"""Tests for ML model views."""
import pytest
from rest_framework import status


@pytest.mark.django_db
class TestMLModelViewSet:
    def test_list_models(self, authenticated_client, ml_model):
        response = authenticated_client.get("/api/v1/ml/models/")
        assert response.status_code == status.HTTP_200_OK

    def test_create_model(self, authenticated_client, dataset):
        data = {
            "name": "New Model",
            "dataset": str(dataset.id),
            "model_type": "random_forest",
            "task_type": "classification",
            "target_column": "label",
            "feature_columns": ["col1", "col2"],
        }
        response = authenticated_client.post("/api/v1/ml/models/", data, format="json")
        assert response.status_code == status.HTTP_201_CREATED
