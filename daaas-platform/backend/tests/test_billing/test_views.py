"""Tests for billing views."""
import pytest
from rest_framework import status


@pytest.mark.django_db
class TestPlanViewSet:
    def test_list_plans(self, api_client, plan):
        response = api_client.get("/api/v1/billing/plans/")
        assert response.status_code == status.HTTP_200_OK
