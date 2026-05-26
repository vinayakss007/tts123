"""Abstract base class for AI providers."""
from abc import ABC, abstractmethod
from typing import Any, AsyncGenerator


class BaseProvider(ABC):
    """Abstract base class for AI provider adapters.

    All AI providers must implement this interface to be compatible
    with the AI gateway router and fallback chain.
    """

    def __init__(self, config: dict):
        """Initialize provider with configuration.

        Args:
            config: Provider configuration dict with api_key, model, base_url, etc.
        """
        self.config = config
        self.model = config.get("model")
        self.api_key = config.get("api_key")
        self.base_url = config.get("base_url")
        self.max_tokens = config.get("max_tokens", 4096)
        self.temperature = config.get("temperature", 0.7)

    @abstractmethod
    async def completion(self, messages: list[dict], **kwargs) -> dict[str, Any]:
        """Generate a completion response.

        Args:
            messages: List of message dicts with 'role' and 'content'.
            **kwargs: Additional options (temperature, max_tokens, etc.)

        Returns:
            Dictionary with:
                - content: The response text
                - model: Model used
                - usage: {prompt_tokens, completion_tokens, total_tokens}
                - provider: Provider name
        """
        pass

    @abstractmethod
    async def stream_completion(self, messages: list[dict], **kwargs) -> AsyncGenerator[dict, None]:
        """Generate a streaming completion response.

        Args:
            messages: List of message dicts with 'role' and 'content'.
            **kwargs: Additional options.

        Yields:
            Dictionaries with chunk data (type, content).
        """
        pass

    @abstractmethod
    async def health_check(self) -> bool:
        """Check if the provider is available and responding.

        Returns:
            True if provider is healthy, False otherwise.
        """
        pass

    def _format_messages(self, messages: list[dict]) -> list[dict]:
        """Format messages for the provider's expected format.

        Override in subclasses if the provider expects a different format.
        """
        return messages

    def _extract_usage(self, response: Any) -> dict[str, int]:
        """Extract token usage from provider response.

        Override in subclasses for provider-specific extraction.
        """
        return {
            "prompt_tokens": 0,
            "completion_tokens": 0,
            "total_tokens": 0,
        }
