"""Tests for accounts models."""
import pytest

from apps.accounts.models import Membership, Organization, User


@pytest.mark.django_db
class TestUserModel:
    """Tests for the User model."""

    def test_create_user(self):
        user = User.objects.create_user(
            email="newuser@example.com",
            password="securepassword",
            first_name="New",
            last_name="User",
        )
        assert user.email == "newuser@example.com"
        assert user.check_password("securepassword")
        assert not user.is_staff

    def test_create_superuser(self):
        user = User.objects.create_superuser(
            email="super@example.com",
            password="superpassword",
            first_name="Super",
            last_name="Admin",
        )
        assert user.is_staff
        assert user.is_superuser

    def test_email_required(self):
        with pytest.raises(ValueError):
            User.objects.create_user(email="", password="test")


@pytest.mark.django_db
class TestOrganizationModel:
    """Tests for the Organization model."""

    def test_create_organization(self, user):
        org = Organization.objects.create(
            name="Test Org",
            slug="test-org-2",
            owner=user,
        )
        assert org.name == "Test Org"
        assert org.plan == Organization.PlanChoices.FREE


@pytest.mark.django_db
class TestMembershipModel:
    """Tests for the Membership model."""

    def test_create_membership(self, user, organization):
        membership = Membership.objects.get(user=user, organization=organization)
        assert membership.role == Membership.RoleChoices.OWNER
