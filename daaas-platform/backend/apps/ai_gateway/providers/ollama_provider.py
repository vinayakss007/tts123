"""Ollama provider adapter for self-hosted models."""
from typing import Any, AsyncGenerator

from django.conf import settings

from .base import BaseProvider


class OllamaProvider(BaseProvider):
    """Ollama adapter for locally-hosted open-source models.

    Supports any model available through Ollama (llama3.1, mistral, codellama, etc.)
    """

    PROVIDER_NAME = "ollama"

    def __init__(self, config: dict):
        super().__init__(config)
        self.base_url = config.get("base_url") or getattr(settings, "OLLAMA_BASE_URL", "http://ollama:11434")
        self.model = config.get("model") or getattr(settings, "OLLAMA_MODEL", "llama3.1")

    async def completion(self, messages: list[dict], **kwargs) -> dict[str, Any]:
        """Generate completion using Ollama API."""
        import httpx

        async with httpx.AsyncClient(base_url=self.base_url, timeout=120.0) as client:
            response = await client.post(
                "/api/chat",
                json={
                    "model": self.model,
                    "messages": self._format_messages(messages),
                    "stream": False,
                    "options": {
                        "temperature": kwargs.get("temperature", self.temperature),
                        "num_predict": kwargs.get("max_tokens", self.max_tokens),
                    },
                },
            )
            response.raise_for_status()
            data = response.json()

        content = data.get("message", {}).get("content", "")
        usage = self._extract_usage_from_ollama(data)

        return {
            "content": content,
            "model": self.model,
            "provider": self.PROVIDER_NAME,
            "usage": usage,
            "finish_reason": "stop",
        }

    async def stream_completion(self, messages: list[dict], **kwargs) -> AsyncGenerator[dict, None]:
        """Stream completion tokens from Ollama API."""
        import httpx

        async with httpx.AsyncClient(base_url=self.base_url, timeout=120.0) as client:
            async with client.stream(
                "POST",
                "/api/chat",
                json={
                    "model": self.model,
                    "messages": self._format_messages(messages),
                    "stream": True,
                    "options": {
                        "temperature": kwargs.get("temperature", self.temperature),
                        "num_predict": kwargs.get("max_tokens", self.max_tokens),
                    },
                },
            ) as response:
                import json

                async for line in response.aiter_lines():
                    if line:
                        data = json.loads(line)
                        if not data.get("done"):
                            content = data.get("message", {}).get("content", "")
                            if content:
                                yield {
                                    "type": "content",
                                    "content": content,
                                    "provider": self.PROVIDER_NAME,
                                }

        yield {"type": "done", "provider": self.PROVIDER_NAME}

    async def health_check(self) -> bool:
        """Check if Ollama server is running and model is available."""
        try:
            import httpx

            async with httpx.AsyncClient(base_url=self.base_url, timeout=5.0) as client:
                response = await client.get("/api/tags")
                return response.status_code == 200
        except Exception:
            return False

    def _extract_usage_from_ollama(self, data: dict) -> dict[str, int]:
        """Extract token usage from Ollama response."""
        prompt_tokens = data.get("prompt_eval_count", 0)
        completion_tokens = data.get("eval_count", 0)
        return {
            "prompt_tokens": prompt_tokens,
            "completion_tokens": completion_tokens,
            "total_tokens": prompt_tokens + completion_tokens,
        }
