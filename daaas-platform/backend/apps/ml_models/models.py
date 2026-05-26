"""Models for ML model training, versioning, and prediction management."""
import uuid

from django.conf import settings
from django.db import models


class MLModel(models.Model):
    """Machine learning model configuration and metadata."""

    class ModelTypeChoices(models.TextChoices):
        LINEAR_REGRESSION = "linear_regression", "Linear Regression"
        LOGISTIC_REGRESSION = "logistic_regression", "Logistic Regression"
        RANDOM_FOREST = "random_forest", "Random Forest"
        GRADIENT_BOOSTING = "gradient_boosting", "Gradient Boosting"
        SVM = "svm", "Support Vector Machine"
        NEURAL_NETWORK = "neural_network", "Neural Network"
        KMEANS = "kmeans", "K-Means Clustering"
        DBSCAN = "dbscan", "DBSCAN"
        AUTO = "auto", "AutoML (Automatic Selection)"

    class TaskTypeChoices(models.TextChoices):
        CLASSIFICATION = "classification", "Classification"
        REGRESSION = "regression", "Regression"
        CLUSTERING = "clustering", "Clustering"
        ANOMALY_DETECTION = "anomaly_detection", "Anomaly Detection"
        TIME_SERIES = "time_series", "Time Series Forecasting"

    class StatusChoices(models.TextChoices):
        DRAFT = "draft", "Draft"
        TRAINING = "training", "Training"
        TRAINED = "trained", "Trained"
        DEPLOYED = "deployed", "Deployed"
        ERROR = "error", "Error"
        ARCHIVED = "archived", "Archived"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    organization = models.ForeignKey(
        "accounts.Organization", on_delete=models.CASCADE, related_name="ml_models"
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True
    )
    dataset = models.ForeignKey(
        "datasets.Dataset", on_delete=models.SET_NULL, null=True, related_name="ml_models"
    )
    model_type = models.CharField(max_length=30, choices=ModelTypeChoices.choices, default=ModelTypeChoices.AUTO)
    task_type = models.CharField(max_length=30, choices=TaskTypeChoices.choices)
    target_column = models.CharField(max_length=255)
    feature_columns = models.JSONField(default=list)
    hyperparameters = models.JSONField(default=dict, blank=True)
    status = models.CharField(max_length=20, choices=StatusChoices.choices, default=StatusChoices.DRAFT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "ML Model"
        verbose_name_plural = "ML Models"

    def __str__(self):
        return f"{self.name} ({self.model_type})"


class TrainingRun(models.Model):
    """Individual training run for a model."""

    class StatusChoices(models.TextChoices):
        QUEUED = "queued", "Queued"
        RUNNING = "running", "Running"
        COMPLETED = "completed", "Completed"
        FAILED = "failed", "Failed"
        CANCELLED = "cancelled", "Cancelled"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    model = models.ForeignKey(MLModel, on_delete=models.CASCADE, related_name="training_runs")
    status = models.CharField(max_length=20, choices=StatusChoices.choices, default=StatusChoices.QUEUED)
    hyperparameters = models.JSONField(default=dict)
    metrics = models.JSONField(default=dict, blank=True, help_text="Training metrics (accuracy, loss, etc.)")
    error_message = models.TextField(blank=True)
    started_at = models.DateTimeField(null=True)
    completed_at = models.DateTimeField(null=True)
    duration_seconds = models.FloatField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Training {self.model.name} - {self.status}"


class ModelVersion(models.Model):
    """Versioned trained model artifact."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    model = models.ForeignKey(MLModel, on_delete=models.CASCADE, related_name="versions")
    training_run = models.OneToOneField(TrainingRun, on_delete=models.CASCADE, related_name="model_version")
    version_number = models.PositiveIntegerField()
    artifact_path = models.CharField(max_length=1024, help_text="Path to model artifact in storage")
    accuracy = models.FloatField(null=True)
    precision = models.FloatField(null=True)
    recall = models.FloatField(null=True)
    f1_score = models.FloatField(null=True)
    feature_importance = models.JSONField(default=dict, blank=True)
    is_active = models.BooleanField(default=False, help_text="Whether this version is deployed")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("model", "version_number")
        ordering = ["-version_number"]

    def __str__(self):
        return f"{self.model.name} v{self.version_number}"


class Prediction(models.Model):
    """Prediction request and result."""

    class StatusChoices(models.TextChoices):
        PENDING = "pending", "Pending"
        COMPLETED = "completed", "Completed"
        ERROR = "error", "Error"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    model = models.ForeignKey(MLModel, on_delete=models.CASCADE, related_name="predictions")
    model_version = models.ForeignKey(ModelVersion, on_delete=models.SET_NULL, null=True)
    input_data = models.JSONField(help_text="Input features for prediction")
    prediction_result = models.JSONField(null=True, blank=True)
    confidence = models.FloatField(null=True)
    status = models.CharField(max_length=20, choices=StatusChoices.choices, default=StatusChoices.PENDING)
    requested_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Prediction for {self.model.name} - {self.status}"
