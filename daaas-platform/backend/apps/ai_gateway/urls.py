"""URL routing for AI gateway."""
from django.urls import path

from .views import AICompletionView, AIStreamingView

urlpatterns = [
    path("completions/", AICompletionView.as_view(), name="ai-completions"),
    path("stream/", AIStreamingView.as_view(), name="ai-stream"),
]
