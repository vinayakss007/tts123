"""Tests for ML model models."""
import pytest

from apps.ml_models.models import MLModel


@pytest.mark.django_db
class TestMLModel:
    def test_create_model(self, ml_model):
        assert ml_model.status == MLModel.StatusChoices.DRAFT
        assert ml_model.task_type == "classification"

    def test_model_str(self, ml_model):
        assert "Test Classifier" in str(ml_model)
