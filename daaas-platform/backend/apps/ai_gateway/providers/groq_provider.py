"""Groq provider adapter."""
from typing import Any, AsyncGenerator

from django.conf import settings

from .base import BaseProvider


class GroqProvider(BaseProvider):
    """Groq API adapter for ultra-fast inference.

    Supports: llama-3.1-70b-versatile, mixtral-8x7b, etc.
    """

    PROVIDER_NAME = "groq"

    def __init__(self, config: dict):
        super().__init__(config)
        self.api_key = config.get("api_key") or getattr(settings, "GROQ_API_KEY", "")
        self.model = config.get("model") or getattr(settings, "GROQ_MODEL", "llama-3.1-70b-versatile")

    async def completion(self, messages: list[dict], **kwargs) -> dict[str, Any]:
        """Generate completion using Groq API (OpenAI-compatible)."""
        from groq import AsyncGroq

        client = AsyncGroq(api_key=self.api_key)

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
        """Stream completion tokens from Groq API."""
        from groq import AsyncGroq

        client = AsyncGroq(api_key=self.api_key)

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
        """Verify Groq API connectivity."""
        try:
            from groq import AsyncGroq

            client = AsyncGroq(api_key=self.api_key)
            await client.models.list()
            return True
        except Exception:
            return False

    def _extract_usage(self, response) -> dict[str, int]:
        """Extract usage from Groq response (OpenAI-compatible format)."""
        if response.usage:
            return {
                "prompt_tokens": response.usage.prompt_tokens,
                "completion_tokens": response.usage.completion_tokens,
                "total_tokens": response.usage.total_tokens,
            }
        return {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}
