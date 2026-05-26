"""OpenAI provider adapter."""
from typing import Any, AsyncGenerator

from django.conf import settings

from .base import BaseProvider


class OpenAIProvider(BaseProvider):
    """OpenAI API adapter supporting GPT models.

    Supports: gpt-4o, gpt-4-turbo, gpt-3.5-turbo, etc.
    """

    PROVIDER_NAME = "openai"

    def __init__(self, config: dict):
        super().__init__(config)
        self.api_key = config.get("api_key") or getattr(settings, "OPENAI_API_KEY", "")
        self.model = config.get("model") or getattr(settings, "OPENAI_MODEL", "gpt-4o")

    async def completion(self, messages: list[dict], **kwargs) -> dict[str, Any]:
        """Generate completion using OpenAI API.

        Args:
            messages: Chat messages in OpenAI format.
            **kwargs: temperature, max_tokens, etc.

        Returns:
            Formatted response with content, usage, and metadata.
        """
        import openai

        client = openai.AsyncOpenAI(api_key=self.api_key)

        response = await client.chat.completions.create(
            model=self.model,
            messages=self._format_messages(messages),
            temperature=kwargs.get("temperature", self.temperature),
            max_tokens=kwargs.get("max_tokens", self.max_tokens),
        )

        choice = response.choices[0]
        usage = self._extract_usage(response)

        return {
            "content": choice.message.content,
            "model": response.model,
            "provider": self.PROVIDER_NAME,
            "usage": usage,
            "finish_reason": choice.finish_reason,
        }

    async def stream_completion(self, messages: list[dict], **kwargs) -> AsyncGenerator[dict, None]:
        """Stream completion tokens from OpenAI API."""
        import openai

        client = openai.AsyncOpenAI(api_key=self.api_key)

        stream = await client.chat.completions.create(
            model=self.model,
            messages=self._format_messages(messages),
            temperature=kwargs.get("temperature", self.temperature),
            max_tokens=kwargs.get("max_tokens", self.max_tokens),
            stream=True,
        )

        async for chunk in stream:
            if chunk.choices and chunk.choices[0].delta.content:
                yield {
                    "type": "content",
                    "content": chunk.choices[0].delta.content,
                    "provider": self.PROVIDER_NAME,
                }

        yield {"type": "done", "provider": self.PROVIDER_NAME}

    async def health_check(self) -> bool:
        """Verify OpenAI API connectivity."""
        try:
            import openai

            client = openai.AsyncOpenAI(api_key=self.api_key)
            await client.models.list()
            return True
        except Exception:
            return False

    def _extract_usage(self, response) -> dict[str, int]:
        """Extract usage from OpenAI response object."""
        if response.usage:
            return {
                "prompt_tokens": response.usage.prompt_tokens,
                "completion_tokens": response.usage.completion_tokens,
                "total_tokens": response.usage.total_tokens,
            }
        return {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}
