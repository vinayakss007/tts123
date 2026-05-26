"""Multi-provider fallback chain with health checks."""
import logging
import time
from typing import Any

from django.conf import settings

from .models import AIProviderConfig
from .providers.base import BaseProvider

logger = logging.getLogger(__name__)


class FallbackChain:
    """Execute AI requests with automatic fallback to alternative providers.

    If the primary provider fails, automatically tries the next provider
    in the priority chain. Includes health checks to skip known-unhealthy providers.
    """

    def __init__(self, organization=None):
        self.organization = organization
        self._health_status: dict[str, ProviderHealth] = {}

    async def execute_with_fallback(
        self, messages: list[dict], excluded_provider: str = None, **kwargs
    ) -> dict[str, Any]:
        """Execute completion with automatic fallback on failure.

        Args:
            messages: Chat messages to send
            excluded_provider: Provider to skip (already tried)
            **kwargs: Additional provider options

        Returns:
            Completion response from the first successful provider.

        Raises:
            AllProvidersFailedError: If all providers in the chain fail.
        """
        providers = self._get_fallback_order(excluded_provider)

        last_error = None
        for provider_name, provider_instance in providers:
            if not self._is_healthy(provider_name):
                logger.info(f"Skipping unhealthy provider: {provider_name}")
                continue

            try:
                start_time = time.time()
                response = await provider_instance.completion(messages, **kwargs)
                latency = time.time() - start_time

                self._mark_healthy(provider_name, latency)
                return response

            except Exception as exc:
                last_error = exc
                self._mark_unhealthy(provider_name, str(exc))
                logger.warning(f"Provider {provider_name} failed: {exc}, trying next...")
                continue

        raise AllProvidersFailedError(
            f"All providers failed. Last error: {last_error}"
        )

    def _get_fallback_order(self, excluded: str = None) -> list[tuple[str, BaseProvider]]:
        """Get ordered list of fallback providers."""
        from .providers import AnthropicProvider, GroqProvider, OllamaProvider, OpenAIProvider

        provider_map = {
            "openai": OpenAIProvider,
            "anthropic": AnthropicProvider,
            "groq": GroqProvider,
            "ollama": OllamaProvider,
        }

        if self.organization:
            configs = AIProviderConfig.objects.filter(
                organization=self.organization,
                is_active=True,
                is_fallback=True,
            ).order_by("priority")

            providers = []
            for config in configs:
                if config.provider == excluded:
                    continue
                cls = provider_map.get(config.provider)
                if cls:
                    providers.append((config.provider, cls(config={})))
            return providers

        # System-level fallback order
        fallback_list = settings.AI_FALLBACK_PROVIDERS
        providers = []
        for name in fallback_list:
            if name == excluded:
                continue
            cls = provider_map.get(name)
            if cls:
                providers.append((name, cls(config={})))
        return providers

    def _is_healthy(self, provider_name: str) -> bool:
        """Check if a provider is considered healthy."""
        health = self._health_status.get(provider_name)
        if not health:
            return True

        if not health.is_healthy:
            # Allow retry after cooldown
            elapsed = time.time() - health.last_failure_time
            return elapsed > health.cooldown_seconds

        return True

    def _mark_healthy(self, provider_name: str, latency: float):
        """Mark a provider as healthy after successful request."""
        self._health_status[provider_name] = ProviderHealth(
            is_healthy=True,
            last_success_time=time.time(),
            latency=latency,
        )

    def _mark_unhealthy(self, provider_name: str, error: str):
        """Mark a provider as unhealthy after failure."""
        health = self._health_status.get(provider_name, ProviderHealth())
        health.is_healthy = False
        health.last_failure_time = time.time()
        health.consecutive_failures += 1
        health.last_error = error
        health.cooldown_seconds = min(300, 30 * health.consecutive_failures)
        self._health_status[provider_name] = health


class ProviderHealth:
    """Track health status of an AI provider."""

    def __init__(self, **kwargs):
        self.is_healthy: bool = kwargs.get("is_healthy", True)
        self.last_success_time: float = kwargs.get("last_success_time", 0)
        self.last_failure_time: float = kwargs.get("last_failure_time", 0)
        self.consecutive_failures: int = kwargs.get("consecutive_failures", 0)
        self.last_error: str = kwargs.get("last_error", "")
        self.latency: float = kwargs.get("latency", 0)
        self.cooldown_seconds: int = kwargs.get("cooldown_seconds", 30)


class AllProvidersFailedError(Exception):
    """Raised when all providers in the fallback chain fail."""

    pass
