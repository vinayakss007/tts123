"""Models for dataset upload, versioning, and metadata management."""
import uuid

from django.conf import settings
from django.db import models


class Dataset(models.Model):
    """Primary dataset entity representing an uploaded data file."""

    class StatusChoices(models.TextChoices):
        UPLOADING = "uploading", "Uploading"
        PROCESSING = "processing", "Processing"
        READY = "ready", "Ready"
        ERROR = "error", "Error"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    organization = models.ForeignKey(
        "accounts.Organization", on_delete=models.CASCADE, related_name="datasets"
    )
    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="datasets"
    )
    file_path = models.CharField(max_length=1024)
    file_name = models.CharField(max_length=255)
    file_size = models.BigIntegerField(help_text="File size in bytes")
    file_type = models.CharField(max_length=50)
    row_count = models.IntegerField(null=True, blank=True)
    column_count = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=StatusChoices.choices, default=StatusChoices.UPLOADING)
    error_message = models.TextField(blank=True)
    tags = models.JSONField(default=list, blank=True)
    metadata = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["organization", "-created_at"]),
            models.Index(fields=["status"]),
        ]

    def __str__(self):
        return f"{self.name} ({self.file_type})"


class DatasetVersion(models.Model):
    """Version tracking for datasets (when data is modified/cleaned)."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE, related_name="versions")
    version_number = models.PositiveIntegerField()
    file_path = models.CharField(max_length=1024)
    change_description = models.TextField(blank=True)
    row_count = models.IntegerField(null=True)
    column_count = models.IntegerField(null=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("dataset", "version_number")
        ordering = ["-version_number"]

    def __str__(self):
        return f"{self.dataset.name} v{self.version_number}"


class DataColumn(models.Model):
    """Metadata about individual columns in a dataset."""

    class DataTypeChoices(models.TextChoices):
        INTEGER = "integer", "Integer"
        FLOAT = "float", "Float"
        STRING = "string", "String"
        BOOLEAN = "boolean", "Boolean"
        DATETIME = "datetime", "DateTime"
        CATEGORICAL = "categorical", "Categorical"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE, related_name="columns")
    name = models.CharField(max_length=255)
    data_type = models.CharField(max_length=20, choices=DataTypeChoices.choices)
    nullable = models.BooleanField(default=True)
    null_count = models.IntegerField(default=0)
    unique_count = models.IntegerField(default=0)
    min_value = models.CharField(max_length=255, blank=True)
    max_value = models.CharField(max_length=255, blank=True)
    mean_value = models.FloatField(null=True, blank=True)
    std_value = models.FloatField(null=True, blank=True)
    sample_values = models.JSONField(default=list, blank=True)
    position = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["position"]
        unique_together = ("dataset", "name")

    def __str__(self):
        return f"{self.dataset.name}.{self.name} ({self.data_type})"


class DataSource(models.Model):
    """External data source connections (database, API, etc.)."""

    class SourceTypeChoices(models.TextChoices):
        POSTGRES = "postgres", "PostgreSQL"
        MYSQL = "mysql", "MySQL"
        MONGODB = "mongodb", "MongoDB"
        API = "api", "REST API"
        S3 = "s3", "S3 Bucket"
        GCS = "gcs", "Google Cloud Storage"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    organization = models.ForeignKey(
        "accounts.Organization", on_delete=models.CASCADE, related_name="data_sources"
    )
    source_type = models.CharField(max_length=20, choices=SourceTypeChoices.choices)
    connection_config = models.JSONField(help_text="Encrypted connection parameters")
    is_active = models.BooleanField(default=True)
    last_synced_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} ({self.source_type})"
