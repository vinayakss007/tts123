"""Serializers for analytics module."""
from rest_framework import serializers

from .models import AnalysisSession, AnalysisStep, CleaningOperation, Visualization


class AnalysisStepSerializer(serializers.ModelSerializer):
    """Serializer for analysis steps."""

    class Meta:
        model = AnalysisStep
        fields = (
            "id", "step_type", "order", "parameters", "result",
            "status", "error_message", "execution_time_ms", "created_at",
        )
        read_only_fields = ("id", "result", "status", "error_message", "execution_time_ms", "created_at")


class VisualizationSerializer(serializers.ModelSerializer):
    """Serializer for visualizations."""

    class Meta:
        model = Visualization
        fields = (
            "id", "title", "description", "chart_type", "config",
            "data", "is_pinned", "created_at", "updated_at",
        )
        read_only_fields = ("id", "data", "created_at", "updated_at")


class AnalysisSessionSerializer(serializers.ModelSerializer):
    """Serializer for analysis sessions."""

    steps = AnalysisStepSerializer(many=True, read_only=True)
    visualizations = VisualizationSerializer(many=True, read_only=True)

    class Meta:
        model = AnalysisSession
        fields = (
            "id", "name", "description", "dataset", "status",
            "config", "results_summary", "steps", "visualizations",
            "created_at", "updated_at",
        )
        read_only_fields = ("id", "status", "results_summary", "created_at", "updated_at")


class CleaningOperationSerializer(serializers.ModelSerializer):
    """Serializer for cleaning operations."""

    class Meta:
        model = CleaningOperation
        fields = (
            "id", "dataset", "operation_type", "parameters",
            "columns_affected", "rows_affected", "status", "created_at",
        )
        read_only_fields = ("id", "rows_affected", "status", "created_at")
