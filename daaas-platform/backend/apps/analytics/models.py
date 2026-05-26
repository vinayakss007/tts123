"""Models for analysis sessions, steps, visualizations, and cleaning operations."""
import uuid

from django.conf import settings
from django.db import models


class AnalysisSession(models.Model):
    """An analysis session containing multiple analysis steps."""

    class StatusChoices(models.TextChoices):
        DRAFT = "draft", "Draft"
        RUNNING = "running", "Running"
        COMPLETED = "completed", "Completed"
        ERROR = "error", "Error"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    dataset = models.ForeignKey(
        "datasets.Dataset", on_delete=models.CASCADE, related_name="analysis_sessions"
    )
    organization = models.ForeignKey(
        "accounts.Organization", on_delete=models.CASCADE, related_name="analysis_sessions"
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True
    )
    status = models.CharField(max_length=20, choices=StatusChoices.choices, default=StatusChoices.DRAFT)
    config = models.JSONField(default=dict, blank=True)
    results_summary = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.dataset.name}"


class AnalysisStep(models.Model):
    """Individual step within an analysis session."""

    class StepTypeChoices(models.TextChoices):
        DESCRIPTIVE_STATS = "descriptive_stats", "Descriptive Statistics"
        CORRELATION = "correlation", "Correlation Analysis"
        DISTRIBUTION = "distribution", "Distribution Analysis"
        HYPOTHESIS_TEST = "hypothesis_test", "Hypothesis Test"
        REGRESSION = "regression", "Regression"
        CLUSTERING = "clustering", "Clustering"
        ANOMALY_DETECTION = "anomaly_detection", "Anomaly Detection"
        CUSTOM = "custom", "Custom Analysis"

    class StatusChoices(models.TextChoices):
        PENDING = "pending", "Pending"
        RUNNING = "running", "Running"
        COMPLETED = "completed", "Completed"
        ERROR = "error", "Error"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    session = models.ForeignKey(AnalysisSession, on_delete=models.CASCADE, related_name="steps")
    step_type = models.CharField(max_length=30, choices=StepTypeChoices.choices)
    order = models.PositiveIntegerField(default=0)
    parameters = models.JSONField(default=dict, blank=True)
    result = models.JSONField(default=dict, blank=True)
    status = models.CharField(max_length=20, choices=StatusChoices.choices, default=StatusChoices.PENDING)
    error_message = models.TextField(blank=True)
    execution_time_ms = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.session.name} - Step {self.order}: {self.step_type}"


class Visualization(models.Model):
    """Chart/visualization configuration and data."""

    class ChartTypeChoices(models.TextChoices):
        LINE = "line", "Line Chart"
        BAR = "bar", "Bar Chart"
        PIE = "pie", "Pie Chart"
        SCATTER = "scatter", "Scatter Plot"
        HISTOGRAM = "histogram", "Histogram"
        HEATMAP = "heatmap", "Heatmap"
        BOX = "box", "Box Plot"
        AREA = "area", "Area Chart"
        TABLE = "table", "Data Table"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    session = models.ForeignKey(
        AnalysisSession, on_delete=models.CASCADE, related_name="visualizations"
    )
    chart_type = models.CharField(max_length=20, choices=ChartTypeChoices.choices)
    config = models.JSONField(default=dict, help_text="Chart configuration (axes, colors, etc.)")
    data = models.JSONField(default=dict, help_text="Chart data payload")
    is_pinned = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.title} ({self.chart_type})"


class CleaningOperation(models.Model):
    """Data cleaning operation applied to a dataset."""

    class OperationTypeChoices(models.TextChoices):
        REMOVE_DUPLICATES = "remove_duplicates", "Remove Duplicates"
        FILL_MISSING = "fill_missing", "Fill Missing Values"
        REMOVE_NULLS = "remove_nulls", "Remove Null Rows"
        NORMALIZE = "normalize", "Normalize"
        STANDARDIZE = "standardize", "Standardize"
        ENCODE_CATEGORICAL = "encode_categorical", "Encode Categorical"
        REMOVE_OUTLIERS = "remove_outliers", "Remove Outliers"
        RENAME_COLUMNS = "rename_columns", "Rename Columns"
        CHANGE_TYPE = "change_type", "Change Data Type"
        CUSTOM = "custom", "Custom Transformation"

    class StatusChoices(models.TextChoices):
        PENDING = "pending", "Pending"
        APPLIED = "applied", "Applied"
        REVERTED = "reverted", "Reverted"
        ERROR = "error", "Error"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    dataset = models.ForeignKey(
        "datasets.Dataset", on_delete=models.CASCADE, related_name="cleaning_operations"
    )
    operation_type = models.CharField(max_length=30, choices=OperationTypeChoices.choices)
    parameters = models.JSONField(default=dict, help_text="Operation-specific parameters")
    columns_affected = models.JSONField(default=list)
    rows_affected = models.IntegerField(default=0)
    status = models.CharField(max_length=20, choices=StatusChoices.choices, default=StatusChoices.PENDING)
    applied_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.operation_type} on {self.dataset.name}"
