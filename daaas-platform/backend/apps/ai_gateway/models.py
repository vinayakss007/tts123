"""Models for AI gateway configuration and usage tracking."""
import uuid

from django.conf import settings
from django.db import models


class AIProviderConfig(models.Model):
    """Configuration for an AI provider within an organization."""

    class ProviderChoices(models.TextChoices):
        OPENAI = "openai", "OpenAI"
        ANTHROPIC = "anthropic", "Anthropic"
        GROQ = "groq", "Groq"
        OLLAMA = "ollama", "Ollama"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    organization = models.ForeignKey(
        "accounts.Organization", on_delete=models.CASCADE, related_name="ai_providers"
    )
    provider = models.CharField(max_length=20, choices=ProviderChoices.choices)
    model_name = models.CharField(max_length=100)
    api_key_encrypted = models.TextField(blank=True, help_text="Encrypted API key")
    base_url = models.URLField(blank=True, help_text="Custom base URL for self-hosted models")
    is_active = models.BooleanField(default=True)
    is_fallback = models.BooleanField(default=False, help_text="Use as fallback provider")
    priority = models.IntegerField(default=0, help_text="Lower = higher priority for fallback")
    max_tokens = models.IntegerField(default=4096)
    temperature = models.FloatField(default=0.7)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("organization", "provider")
        ordering = ["priority"]

    def __str__(self):
        return f"{self.organization.name} - {self.provider} ({self.model_name})"


class AIUsageLog(models.Model):
    """Log of AI API usage for tracking and billing."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    organization = models.ForeignKey(
        "accounts.Organization", on_delete=models.CASCADE, related_name="ai_usage_logs"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True
    )
    provider = models.CharField(max_length=20, choices=AIProviderConfig.ProviderChoices.choices)
    model_name = models.CharField(max_length=100)
    prompt_tokens = models.IntegerField(default=0)
    completion_tokens = models.IntegerField(default=0)
    total_tokens = models.IntegerField(default=0)
    latency_ms = models.IntegerField(default=0)
    status = models.CharField(max_length=20, default="success")
    error_message = models.TextField(blank=True)
    request_type = models.CharField(max_length=50, help_text="e.g., analysis, report, cleaning")
    metadata = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["organization", "-created_at"]),
            models.Index(fields=["provider", "-created_at"]),
        ]

    def __str__(self):
        return f"{self.provider} - {self.total_tokens} tokens"


class PromptTemplate(models.Model):
    """Reusable AI prompt templates."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    template = models.TextField(help_text="Prompt template with {variable} placeholders")
    system_prompt = models.TextField(blank=True, help_text="System message for the AI")
    category = models.CharField(max_length=50, help_text="e.g., analysis, cleaning, report")
    is_system = models.BooleanField(default=False)
    organization = models.ForeignKey(
        "accounts.Organization", on_delete=models.CASCADE, null=True, blank=True
    )
    variables = models.JSONField(default=list, help_text="List of expected template variables")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["category", "name"]

    def __str__(self):
        return f"{self.name} ({self.category})"

    def render(self, **kwargs) -> str:
        """Render the template with provided variables."""
        return self.template.format(**kwargs)
