"""Conftest for billing tests."""
import pytest
from decimal import Decimal

from apps.billing.models import Plan, Subscription


@pytest.fixture
def plan(db):
    """Create a test plan."""
    return Plan.objects.create(
        name="Starter",
        tier=Plan.TierChoices.STARTER,
        price_monthly=Decimal("29.00"),
        price_yearly=Decimal("290.00"),
        max_datasets=50,
        max_storage_gb=10,
        max_ai_tokens_monthly=100000,
    )


@pytest.fixture
def subscription(db, organization, plan):
    """Create a test subscription."""
    return Subscription.objects.create(
        organization=organization,
        plan=plan,
        status=Subscription.StatusChoices.ACTIVE,
    )
