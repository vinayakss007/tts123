"""Serializers for notifications."""
from rest_framework import serializers

from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    """Serializer for notification data."""

    class Meta:
        model = Notification
        fields = (
            "id", "title", "message", "notification_type", "category",
            "is_read", "action_url", "metadata", "created_at",
        )
        read_only_fields = ("id", "title", "message", "notification_type", "category", "created_at")
