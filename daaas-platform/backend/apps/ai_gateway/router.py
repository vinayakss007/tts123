"""AI request router - routes requests to the appropriate provider."""
from typing import Any

from django.conf import settings

from .fallback import FallbackChain
from .models import AIProviderConfig
from .providers import AnthropicProvider, GroqProvider, OllamaProvider, OpenAIProvider
from .providers.base import BaseProvider
from .token_tracker import TokenTracker


class AIRouter:
    """Routes AI requests to the appropriate provider based on configuration.

    Supports:
    - Organization-specific provider configuration
    - Automatic fallback to alternative providers on failure
    - Token budget enforcement
    - Request/response logging
    """

    PROVIDER_MAP = {
        "openai": OpenAIProvider,
        "anthropic": AnthropicProvider,
        "groq": GroqProvider,
        "ollama": OllamaProvider,
    }

    def __init__(self, organization=None):
        self.organization = organization
        self.token_tracker = TokenTracker(organization)
        self.fallback_chain = FallbackChain(organization)

    def get_provider(self, provider_name: str = None) -> BaseProvider:
        """Get the appropriate provider instance.

        Args:
            provider_name: Optional override for provider selection.
                          Uses organization default or system default if not specified.

        Returns:
            Configured provider instance.
        """
        if not provider_name:
            provider_name = self._get_default_provider()

        provider_class = self.PROVIDER_MAP.get(provider_name)
        if not provider_class:
            raise ValueError(f"Unknown AI provider: {provider_name}")

        config = self._get_provider_config(provider_name)
        return provider_class(config=config)

    async def completion(self, messages: list[dict], **kwargs) -> dict[str, Any]:
        """Route a completion request to the appropriate provider.

        Handles provider selection, token budget checks, and fallback.
        """
        # Check token budget
        if not self.token_tracker.has_budget():
            raise TokenBudgetExceededError("Monthly AI token budget exceeded")

        provider_name = kwargs.pop("provider", None)
        provider = self.get_provider(provider_name)

        try:
            response = await provider.completion(messages, **kwargs)
            self.token_tracker.record_usage(response.get("usage", {}))
            return response
        except Exception as exc:
            # Try fallback chain
            return await self.fallback_chain.execute_with_fallback(
                messages, excluded_provider=provider_name, **kwargs
            )

    async def stream_completion(self, messages: list[dict], **kwargs):
        """Route a streaming completion request to the appropriate provider.

        Yields chunks as they arrive from the provider.
        """
        provider_name = kwargs.pop("provider", None)
        provider = self.get_provider(provider_name)

        async for chunk in provider.stream_completion(messages, **kwargs):
            yield chunk

    def _get_default_provider(self) -> str:
        """Get the default provider for the organization or system."""
        if self.organization:
            config = AIProviderConfig.objects.filter(
                organization=self.organization,
                is_active=True,
            ).order_by("priority").first()
            if config:
                return config.provider

        return settings.AI_DEFAULT_PROVIDER

    def _get_provider_config(self, provider_name: str) -> dict:
        """Get provider configuration from org settings or system defaults."""
        if self.organization:
            try:
                config = AIProviderConfig.objects.get(
                    organization=self.organization,
                    provider=provider_name,
                    is_active=True,
                )
                return {
                    "model": config.model_name,
                    "api_key": config.api_key_encrypted,
                    "base_url": config.base_url,
                    "max_tokens": config.max_tokens,
                    "temperature": config.temperature,
                }
            except AIProviderConfig.DoesNotExist:
                pass

        # Fall back to system-level configuration
        return {"model": None, "api_key": None}


class TokenBudgetExceededError(Exception):
    """Raised when an organization exceeds their AI token budget."""

    pass
