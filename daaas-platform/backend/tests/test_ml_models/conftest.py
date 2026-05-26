"""Conftest for ML models tests."""
import pytest

from apps.ml_models.models import MLModel


@pytest.fixture
def ml_model(db, organization, user, dataset):
    """Create a test ML model."""
    return MLModel.objects.create(
        name="Test Classifier",
        organization=organization,
        created_by=user,
        dataset=dataset,
        model_type=MLModel.ModelTypeChoices.RANDOM_FOREST,
        task_type=MLModel.TaskTypeChoices.CLASSIFICATION,
        target_column="label",
        feature_columns=["feature_1", "feature_2"],
    )
