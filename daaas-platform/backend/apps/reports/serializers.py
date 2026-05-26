"""Serializers for reports module."""
from rest_framework import serializers

from .models import Report, ReportSection, ReportTemplate


class ReportSectionSerializer(serializers.ModelSerializer):
    """Serializer for report sections."""

    class Meta:
        model = ReportSection
        fields = ("id", "title", "content", "section_type", "order", "visualization_config", "ai_generated")
        read_only_fields = ("id",)


class ReportSerializer(serializers.ModelSerializer):
    """Serializer for report CRUD."""

    sections = ReportSectionSerializer(many=True, read_only=True)

    class Meta:
        model = Report
        fields = (
            "id", "title", "description", "template", "dataset",
            "analysis_session", "status", "output_format", "file_path",
            "ai_tokens_used", "sections", "created_at", "updated_at",
        )
        read_only_fields = ("id", "status", "file_path", "ai_tokens_used", "created_at", "updated_at")


class ReportTemplateSerializer(serializers.ModelSerializer):
    """Serializer for report templates."""

    class Meta:
        model = ReportTemplate
        fields = ("id", "name", "description", "structure", "prompt_template", "is_system", "created_at")
        read_only_fields = ("id", "is_system", "created_at")


class GenerateReportSerializer(serializers.Serializer):
    """Serializer for report generation request."""

    template_id = serializers.UUIDField(required=False)
    dataset_id = serializers.UUIDField()
    analysis_session_id = serializers.UUIDField(required=False)
    title = serializers.CharField(max_length=255)
    output_format = serializers.ChoiceField(choices=["pdf", "html", "markdown"], default="html")
    custom_instructions = serializers.CharField(required=False, allow_blank=True)
