"""Serializers for AI gateway requests and responses."""
from rest_framework import serializers


class AIMessageSerializer(serializers.Serializer):
    """Serializer for a single AI message."""

    role = serializers.ChoiceField(choices=["system", "user", "assistant"])
    content = serializers.CharField()


class AICompletionRequestSerializer(serializers.Serializer):
    """Serializer for AI completion requests."""

    messages = AIMessageSerializer(many=True)
    provider = serializers.ChoiceField(
        choices=["openai", "anthropic", "groq", "ollama"],
        required=False,
    )
    model = serializers.CharField(required=False)
    max_tokens = serializers.IntegerField(default=4096, min_value=1, max_value=128000)
    temperature = serializers.FloatField(default=0.7, min_value=0.0, max_value=2.0)
    stream = serializers.BooleanField(default=False)


class AICompletionResponseSerializer(serializers.Serializer):
    """Serializer for AI completion responses."""

    content = serializers.CharField()
    provider = serializers.CharField()
    model = serializers.CharField()
    usage = serializers.DictField()
    latency_ms = serializers.IntegerField()
