"""Tests for report views."""
import pytest
from rest_framework import status


@pytest.mark.django_db
class TestReportViewSet:
    def test_list_reports(self, authenticated_client, report):
        response = authenticated_client.get("/api/v1/reports/reports/")
        assert response.status_code == status.HTTP_200_OK

    def test_unauthenticated_access(self, api_client):
        response = api_client.get("/api/v1/reports/reports/")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
