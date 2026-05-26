"""Tests for billing models."""
import pytest
from decimal import Decimal

from apps.billing.models import Plan, Subscription


@pytest.mark.django_db
class TestPlanModel:
    def test_create_plan(self, plan):
        assert plan.tier == "starter"
        assert plan.price_monthly == Decimal("29.00")


@pytest.mark.django_db
class TestSubscriptionModel:
    def test_create_subscription(self, subscription):
        assert subscription.status == "active"
