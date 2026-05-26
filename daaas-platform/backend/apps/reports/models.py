"""Models for AI-powered report generation."""
import uuid

from django.conf import settings
from django.db import models


class ReportTemplate(models.Model):
    """Reusable report template."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    structure = models.JSONField(default=list, help_text="Template section structure")
    prompt_template = models.TextField(help_text="AI prompt template with variables")
    is_system = models.BooleanField(default=False, help_text="System-provided template")
    organization = models.ForeignKey(
        "accounts.Organization", on_delete=models.CASCADE, null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Report(models.Model):
    """Generated report instance."""

    class StatusChoices(models.TextChoices):
        DRAFT = "draft", "Draft"
        GENERATING = "generating", "Generating"
        COMPLETED = "completed", "Completed"
        ERROR = "error", "Error"

    class FormatChoices(models.TextChoices):
        PDF = "pdf", "PDF"
        HTML = "html", "HTML"
        MARKDOWN = "markdown", "Markdown"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    organization = models.ForeignKey(
        "accounts.Organization", on_delete=models.CASCADE, related_name="reports"
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True
    )
    template = models.ForeignKey(
        ReportTemplate, on_delete=models.SET_NULL, null=True, blank=True
    )
    dataset = models.ForeignKey(
        "datasets.Dataset", on_delete=models.SET_NULL, null=True, related_name="reports"
    )
    analysis_session = models.ForeignKey(
        "analytics.AnalysisSession", on_delete=models.SET_NULL, null=True, blank=True
    )
    status = models.CharField(max_length=20, choices=StatusChoices.choices, default=StatusChoices.DRAFT)
    output_format = models.CharField(max_length=20, choices=FormatChoices.choices, default=FormatChoices.HTML)
    file_path = models.CharField(max_length=1024, blank=True)
    ai_tokens_used = models.IntegerField(default=0)
    error_message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class ReportSection(models.Model):
    """Individual section within a report."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    report = models.ForeignKey(Report, on_delete=models.CASCADE, related_name="sections")
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    section_type = models.CharField(max_length=50, default="text")
    order = models.PositiveIntegerField(default=0)
    visualization_config = models.JSONField(default=dict, blank=True)
    ai_generated = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.report.title} - {self.title}"
