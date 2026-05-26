"""Models for the notification system."""
import uuid

from django.conf import settings
from django.db import models


class Notification(models.Model):
    """User notification for real-time updates."""

    class TypeChoices(models.TextChoices):
        INFO = "info", "Information"
        SUCCESS = "success", "Success"
        WARNING = "warning", "Warning"
        ERROR = "error", "Error"

    class CategoryChoices(models.TextChoices):
        DATASET = "dataset", "Dataset"
        ANALYSIS = "analysis", "Analysis"
        ML_MODEL = "ml_model", "ML Model"
        REPORT = "report", "Report"
        BILLING = "billing", "Billing"
        SYSTEM = "system", "System"
        COLLABORATION = "collaboration", "Collaboration"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notifications"
    )
    title = models.CharField(max_length=255)
    message = models.TextField()
    notification_type = models.CharField(max_length=20, choices=TypeChoices.choices, default=TypeChoices.INFO)
    category = models.CharField(max_length=20, choices=CategoryChoices.choices, default=CategoryChoices.SYSTEM)
    is_read = models.BooleanField(default=False)
    action_url = models.CharField(max_length=500, blank=True, help_text="URL for notification action")
    metadata = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["user", "is_read", "-created_at"]),
        ]

    def __str__(self):
        return f"{self.title} - {self.user.email}"
