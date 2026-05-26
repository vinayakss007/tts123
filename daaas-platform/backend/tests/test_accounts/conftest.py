"""Conftest for accounts tests."""
import pytest

from apps.accounts.models import Invitation, Membership, Organization, User


@pytest.fixture
def admin_user(db):
    """Create an admin user."""
    return User.objects.create_user(
        email="admin@example.com",
        password="adminpassword123",
        first_name="Admin",
        last_name="User",
        is_staff=True,
    )


@pytest.fixture
def second_user(db):
    """Create a second test user."""
    return User.objects.create_user(
        email="user2@example.com",
        password="testpassword123",
        first_name="Second",
        last_name="User",
    )
