"""Views for AI gateway endpoints."""
import time

from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .router import AIRouter
from .serializers import AICompletionRequestSerializer, AICompletionResponseSerializer
from .streaming import StreamingHandler


class AICompletionView(APIView):
    """AI completion endpoint supporting both sync and streaming."""

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        """Handle AI completion request."""
        serializer = AICompletionRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        router = AIRouter(organization=request.user.last_active_organization)

        if data.get("stream"):
            return self._handle_streaming(router, data)
        else:
            return self._handle_sync(router, data)

    def _handle_sync(self, router: AIRouter, data: dict) -> Response:
        """Handle synchronous completion request."""
        start_time = time.time()

        # In production, this would be async
        # response = await router.completion(data["messages"], **kwargs)
        response = {
            "content": "AI completion placeholder",
            "provider": data.get("provider", "openai"),
            "model": data.get("model", ""),
            "usage": {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0},
        }

        latency_ms = int((time.time() - start_time) * 1000)
        response["latency_ms"] = latency_ms

        return Response(response, status=status.HTTP_200_OK)

    def _handle_streaming(self, router: AIRouter, data: dict):
        """Handle streaming completion request via SSE."""
        handler = StreamingHandler()
        # In production, would pass async generator from router.stream_completion
        # For now, return a placeholder

        async def mock_generator():
            yield {"type": "content", "content": "Streaming not yet implemented"}
            yield {"type": "done"}

        return handler.create_sse_response(mock_generator())


class AIStreamingView(APIView):
    """Dedicated streaming endpoint for AI responses."""

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        """Handle streaming AI completion request."""
        serializer = AICompletionRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        router = AIRouter(organization=request.user.last_active_organization)
        handler = StreamingHandler()

        async def stream():
            async for chunk in router.stream_completion(data["messages"]):
                yield chunk

        return handler.create_sse_response(stream())
