"""Tests for analytics views."""
import pytest
from rest_framework import status


@pytest.mark.django_db
class TestAnalysisSessionViewSet:
    def test_list_sessions(self, authenticated_client, analysis_session):
        response = authenticated_client.get("/api/v1/analytics/sessions/")
        assert response.status_code == status.HTTP_200_OK

    def test_unauthenticated_access(self, api_client):
        response = api_client.get("/api/v1/analytics/sessions/")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
