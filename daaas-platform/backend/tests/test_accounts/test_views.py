"""Tests for accounts views."""
import pytest
from rest_framework import status


@pytest.mark.django_db
class TestRegistration:
    """Tests for user registration endpoint."""

    def test_register_success(self, api_client):
        data = {
            "email": "newuser@example.com",
            "first_name": "New",
            "last_name": "User",
            "password": "securepassword123",
            "password_confirm": "securepassword123",
        }
        response = api_client.post("/api/v1/accounts/register/", data)
        assert response.status_code == status.HTTP_201_CREATED
        assert "tokens" in response.data

    def test_register_password_mismatch(self, api_client):
        data = {
            "email": "newuser@example.com",
            "first_name": "New",
            "last_name": "User",
            "password": "securepassword123",
            "password_confirm": "differentpassword",
        }
        response = api_client.post("/api/v1/accounts/register/", data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
class TestUserProfile:
    """Tests for user profile endpoint."""

    def test_get_profile(self, authenticated_client, user):
        response = authenticated_client.get("/api/v1/accounts/users/me/")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["email"] == user.email

    def test_unauthenticated_access(self, api_client):
        response = api_client.get("/api/v1/accounts/users/me/")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
