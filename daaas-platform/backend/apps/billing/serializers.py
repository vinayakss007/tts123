"""Serializers for billing module."""
from rest_framework import serializers

from .models import Invoice, Plan, Subscription, UsageRecord


class PlanSerializer(serializers.ModelSerializer):
    """Serializer for subscription plans."""

    class Meta:
        model = Plan
        fields = (
            "id", "name", "tier", "price_monthly", "price_yearly",
            "max_datasets", "max_storage_gb", "max_ai_tokens_monthly",
            "max_ml_training_runs", "max_team_members", "max_reports_monthly",
            "custom_branding", "priority_support", "api_access",
        )


class SubscriptionSerializer(serializers.ModelSerializer):
    """Serializer for subscription management."""

    plan = PlanSerializer(read_only=True)

    class Meta:
        model = Subscription
        fields = (
            "id", "plan", "status", "billing_interval",
            "trial_ends_at", "current_period_start", "current_period_end",
            "cancelled_at", "created_at",
        )
        read_only_fields = fields


class UsageRecordSerializer(serializers.ModelSerializer):
    """Serializer for usage records."""

    class Meta:
        model = UsageRecord
        fields = ("id", "metric", "quantity", "period_start", "period_end", "created_at")
        read_only_fields = fields


class InvoiceSerializer(serializers.ModelSerializer):
    """Serializer for invoices."""

    class Meta:
        model = Invoice
        fields = ("id", "amount", "currency", "status", "description", "period_start", "period_end", "paid_at", "pdf_url", "created_at")
        read_only_fields = fields


class CreateCheckoutSerializer(serializers.Serializer):
    """Serializer for creating a checkout session."""

    plan_tier = serializers.ChoiceField(choices=["starter", "professional", "enterprise"])
    billing_interval = serializers.ChoiceField(choices=["monthly", "yearly"], default="monthly")
