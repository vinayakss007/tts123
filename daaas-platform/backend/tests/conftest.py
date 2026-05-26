"""Root conftest for backend test suite."""
import pytest
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    """Return an unauthenticated API client."""
    return APIClient()


@pytest.fixture
def authenticated_client(api_client, user):
    """Return an authenticated API client."""
    api_client.force_authenticate(user=user)
    return api_client


@pytest.fixture
def user(db):
    """Create and return a test user."""
    from apps.accounts.models import User

    return User.objects.create_user(
        email="test@example.com",
        password="testpassword123",
        first_name="Test",
        last_name="User",
    )


@pytest.fixture
def organization(db, user):
    """Create and return a test organization."""
    from apps.accounts.models import Membership, Organization

    org = Organization.objects.create(
        name="Test Organization",
        slug="test-org",
        owner=user,
    )
    Membership.objects.create(
        user=user,
        organization=org,
        role=Membership.RoleChoices.OWNER,
    )
    user.last_active_organization = org
    user.save(update_fields=["last_active_organization"])
    return org
