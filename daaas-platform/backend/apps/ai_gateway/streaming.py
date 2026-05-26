"""SSE/WebSocket streaming handler for AI responses."""
import asyncio
import json
from typing import AsyncGenerator

from django.http import StreamingHttpResponse


class StreamingHandler:
    """Handle streaming AI responses via Server-Sent Events (SSE).

    Provides real-time token-by-token delivery of AI responses to the frontend.
    """

    def create_sse_response(self, generator: AsyncGenerator) -> StreamingHttpResponse:
        """Create an SSE streaming response from an async generator.

        Args:
            generator: Async generator yielding response chunks.

        Returns:
            StreamingHttpResponse with SSE content type.
        """
        response = StreamingHttpResponse(
            self._sse_stream(generator),
            content_type="text/event-stream",
        )
        response["Cache-Control"] = "no-cache"
        response["X-Accel-Buffering"] = "no"
        return response

    async def _sse_stream(self, generator: AsyncGenerator):
        """Format generator output as SSE events."""
        try:
            async for chunk in generator:
                if isinstance(chunk, dict):
                    data = json.dumps(chunk)
                else:
                    data = json.dumps({"content": chunk})

                yield f"data: {data}\n\n"

            # Send completion event
            yield f"data: {json.dumps({'type': 'done'})}\n\n"

        except Exception as exc:
            error_data = json.dumps({"type": "error", "message": str(exc)})
            yield f"data: {error_data}\n\n"

    def format_chunk(self, content: str, chunk_type: str = "content") -> dict:
        """Format a streaming chunk for transmission.

        Args:
            content: The content of the chunk.
            chunk_type: Type of chunk (content, tool_call, metadata).

        Returns:
            Formatted chunk dictionary.
        """
        return {
            "type": chunk_type,
            "content": content,
        }

    def format_usage(self, prompt_tokens: int, completion_tokens: int) -> dict:
        """Format usage data for the final streaming message."""
        return {
            "type": "usage",
            "prompt_tokens": prompt_tokens,
            "completion_tokens": completion_tokens,
            "total_tokens": prompt_tokens + completion_tokens,
        }
