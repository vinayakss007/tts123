"""Serializers for ML models module."""
from rest_framework import serializers

from .models import MLModel, ModelVersion, Prediction, TrainingRun


class TrainingRunSerializer(serializers.ModelSerializer):
    """Serializer for training runs."""

    class Meta:
        model = TrainingRun
        fields = (
            "id", "status", "hyperparameters", "metrics", "error_message",
            "started_at", "completed_at", "duration_seconds", "created_at",
        )
        read_only_fields = (
            "id", "metrics", "error_message", "started_at",
            "completed_at", "duration_seconds", "created_at",
        )


class ModelVersionSerializer(serializers.ModelSerializer):
    """Serializer for model versions."""

    class Meta:
        model = ModelVersion
        fields = (
            "id", "version_number", "accuracy", "precision", "recall",
            "f1_score", "feature_importance", "is_active", "created_at",
        )
        read_only_fields = fields


class MLModelSerializer(serializers.ModelSerializer):
    """Serializer for ML model CRUD operations."""

    latest_version = serializers.SerializerMethodField()
    training_runs_count = serializers.SerializerMethodField()

    class Meta:
        model = MLModel
        fields = (
            "id", "name", "description", "model_type", "task_type",
            "target_column", "feature_columns", "hyperparameters",
            "status", "dataset", "latest_version", "training_runs_count",
            "created_at", "updated_at",
        )
        read_only_fields = ("id", "status", "created_at", "updated_at")

    def get_latest_version(self, obj):
        version = obj.versions.filter(is_active=True).first()
        if version:
            return ModelVersionSerializer(version).data
        return None

    def get_training_runs_count(self, obj):
        return obj.training_runs.count()


class TrainModelSerializer(serializers.Serializer):
    """Serializer for triggering model training."""

    hyperparameters = serializers.DictField(required=False, default=dict)
    test_size = serializers.FloatField(default=0.2, min_value=0.1, max_value=0.5)
    cross_validation_folds = serializers.IntegerField(default=5, min_value=2, max_value=10)


class PredictionSerializer(serializers.ModelSerializer):
    """Serializer for prediction requests."""

    class Meta:
        model = Prediction
        fields = (
            "id", "model", "model_version", "input_data",
            "prediction_result", "confidence", "status", "created_at",
        )
        read_only_fields = ("id", "prediction_result", "confidence", "status", "created_at")


class PredictionRequestSerializer(serializers.Serializer):
    """Serializer for batch prediction requests."""

    input_data = serializers.ListField(
        child=serializers.DictField(),
        help_text="List of input feature dictionaries",
    )
