"""Serializers for dataset management."""
from rest_framework import serializers

from .models import DataColumn, DataSource, Dataset, DatasetVersion


class DataColumnSerializer(serializers.ModelSerializer):
    """Serializer for dataset column metadata."""

    class Meta:
        model = DataColumn
        fields = (
            "id", "name", "data_type", "nullable", "null_count",
            "unique_count", "min_value", "max_value", "mean_value",
            "std_value", "sample_values", "position",
        )
        read_only_fields = ("id",)


class DatasetVersionSerializer(serializers.ModelSerializer):
    """Serializer for dataset versions."""

    class Meta:
        model = DatasetVersion
        fields = ("id", "version_number", "change_description", "row_count", "column_count", "created_at")
        read_only_fields = ("id", "version_number", "created_at")


class DatasetSerializer(serializers.ModelSerializer):
    """Serializer for dataset CRUD operations."""

    columns = DataColumnSerializer(many=True, read_only=True)
    uploaded_by_email = serializers.EmailField(source="uploaded_by.email", read_only=True)

    class Meta:
        model = Dataset
        fields = (
            "id", "name", "description", "file_name", "file_size",
            "file_type", "row_count", "column_count", "status",
            "tags", "metadata", "columns", "uploaded_by_email",
            "created_at", "updated_at",
        )
        read_only_fields = (
            "id", "file_size", "file_type", "row_count", "column_count",
            "status", "columns", "uploaded_by_email", "created_at", "updated_at",
        )


class DatasetUploadSerializer(serializers.Serializer):
    """Serializer for file upload."""

    file = serializers.FileField()
    name = serializers.CharField(max_length=255, required=False)
    description = serializers.CharField(required=False, allow_blank=True)
    tags = serializers.ListField(child=serializers.CharField(), required=False)


class DataSourceSerializer(serializers.ModelSerializer):
    """Serializer for external data sources."""

    class Meta:
        model = DataSource
        fields = ("id", "name", "source_type", "connection_config", "is_active", "last_synced_at", "created_at")
        read_only_fields = ("id", "last_synced_at", "created_at")
