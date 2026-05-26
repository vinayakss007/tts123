"""Anthropic provider adapter."""
from typing import Any, AsyncGenerator

from django.conf import settings

from .base import BaseProvider


class AnthropicProvider(BaseProvider):
    """Anthropic API adapter supporting Claude models.

    Supports: claude-3-5-sonnet, claude-3-opus, claude-3-haiku, etc.
    """

    PROVIDER_NAME = "anthropic"

    def __init__(self, config: dict):
        super().__init__(config)
        self.api_key = config.get("api_key") or getattr(settings, "ANTHROPIC_API_KEY", "")
        self.model = config.get("model") or getattr(settings, "ANTHROPIC_MODEL", "claude-3-5-sonnet-20241022")

    async def completion(self, messages: list[dict], **kwargs) -> dict[str, Any]:
        """Generate completion using Anthropic API.

        Anthropic uses a different message format with a separate system parameter.
        """
        import anthropic

        client = anthropic.AsyncAnthropic(api_key=self.api_key)

        # Extract system message from messages list
        system_message = ""
        chat_messages = []
        for msg in messages:
            if msg["role"] == "system":
                system_message = msg["content"]
            else:
                chat_messages.append(msg)

        response = await client.messages.create(
            model=self.model,
            system=system_message,
            messages=chat_messages,
            temperature=kwargs.get("temperature", self.temperature),
            max_tokens=kwargs.get("max_tokens", self.max_tokens),
        )

        content = response.content[0].text if response.content else ""
        usage = self._extract_usage(response)

        return {
            "content": content,
            "model": response.model,
            "provider": self.PROVIDER_NAME,
            "usage": usage,
            "finish_reason": response.stop_reason,
        }

    async def stream_completion(self, messages: list[dict], **kwargs) -> AsyncGenerator[dict, None]:
        """Stream completion tokens from Anthropic API."""
        import anthropic

        client = anthropic.AsyncAnthropic(api_key=self.api_key)

        system_message = ""
        chat_messages = []
        for msg in messages:
            if msg["role"] == "system":
                system_message = msg["content"]
            else:
                chat_messages.append(msg)

        async with client.messages.stream(
            model=self.model,
            system=system_message,
            messages=chat_messages,
            temperature=kwargs.get("temperature", self.temperature),
            max_tokens=kwargs.get("max_tokens", self.max_tokens),
        ) as stream:
            async for text in stream.text_stream:
                yield {
                    "type": "content",
                    "content": text,
                    "provider": self.PROVIDER_NAME,
                }

        yield {"type": "done", "provider": self.PROVIDER_NAME}

    async def health_check(self) -> bool:
        """Verify Anthropic API connectivity."""
        try:
            import anthropic

            client = anthropic.AsyncAnthropic(api_key=self.api_key)
            await client.messages.create(
                model=self.model,
                messages=[{"role": "user", "content": "ping"}],
                max_tokens=5,
            )
            return True
        except Exception:
            return False

    def _extract_usage(self, response) -> dict[str, int]:
        """Extract usage from Anthropic response."""
        if response.usage:
            return {
                "prompt_tokens": response.usage.input_tokens,
                "completion_tokens": response.usage.output_tokens,
                "total_tokens": response.usage.input_tokens + response.usage.output_tokens,
            }
        return {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}
