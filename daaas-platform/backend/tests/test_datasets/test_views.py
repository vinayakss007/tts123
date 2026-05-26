"""Tests for dataset views."""
import pytest
from rest_framework import status


@pytest.mark.django_db
class TestDatasetViewSet:
    """Tests for dataset API endpoints."""

    def test_list_datasets(self, authenticated_client, dataset):
        response = authenticated_client.get("/api/v1/datasets/datasets/")
        assert response.status_code == status.HTTP_200_OK

    def test_retrieve_dataset(self, authenticated_client, dataset):
        response = authenticated_client.get(f"/api/v1/datasets/datasets/{dataset.id}/")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["name"] == "Test Dataset"

    def test_unauthenticated_access(self, api_client):
        response = api_client.get("/api/v1/datasets/datasets/")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
