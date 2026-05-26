"""Models for subscription, payment, and usage management."""
import uuid

from django.db import models


class Plan(models.Model):
    """Subscription plan definition."""

    class TierChoices(models.TextChoices):
        FREE = "free", "Free"
        STARTER = "starter", "Starter"
        PROFESSIONAL = "professional", "Professional"
        ENTERPRISE = "enterprise", "Enterprise"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    tier = models.CharField(max_length=20, choices=TierChoices.choices, unique=True)
    stripe_price_id = models.CharField(max_length=255, blank=True)
    price_monthly = models.DecimalField(max_digits=10, decimal_places=2)
    price_yearly = models.DecimalField(max_digits=10, decimal_places=2)

    # Feature limits
    max_datasets = models.IntegerField(default=5)
    max_storage_gb = models.IntegerField(default=1)
    max_ai_tokens_monthly = models.IntegerField(default=10000)
    max_ml_training_runs = models.IntegerField(default=5)
    max_team_members = models.IntegerField(default=1)
    max_reports_monthly = models.IntegerField(default=5)
    custom_branding = models.BooleanField(default=False)
    priority_support = models.BooleanField(default=False)
    api_access = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["price_monthly"]

    def __str__(self):
        return f"{self.name} (${self.price_monthly}/mo)"


class Subscription(models.Model):
    """Organization subscription to a plan."""

    class StatusChoices(models.TextChoices):
        ACTIVE = "active", "Active"
        TRIALING = "trialing", "Trialing"
        PAST_DUE = "past_due", "Past Due"
        CANCELLED = "cancelled", "Cancelled"
        PAUSED = "paused", "Paused"

    class IntervalChoices(models.TextChoices):
        MONTHLY = "monthly", "Monthly"
        YEARLY = "yearly", "Yearly"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    organization = models.OneToOneField(
        "accounts.Organization", on_delete=models.CASCADE, related_name="subscription"
    )
    plan = models.ForeignKey(Plan, on_delete=models.PROTECT, related_name="subscriptions")
    status = models.CharField(max_length=20, choices=StatusChoices.choices, default=StatusChoices.TRIALING)
    billing_interval = models.CharField(max_length=10, choices=IntervalChoices.choices, default=IntervalChoices.MONTHLY)
    stripe_subscription_id = models.CharField(max_length=255, blank=True)
    stripe_customer_id = models.CharField(max_length=255, blank=True)
    trial_ends_at = models.DateTimeField(null=True, blank=True)
    current_period_start = models.DateTimeField(null=True)
    current_period_end = models.DateTimeField(null=True)
    cancelled_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.organization.name} - {self.plan.name}"


class UsageRecord(models.Model):
    """Track resource usage for metering and billing."""

    class MetricChoices(models.TextChoices):
        AI_TOKENS = "ai_tokens", "AI Tokens"
        STORAGE_BYTES = "storage_bytes", "Storage (Bytes)"
        ML_TRAINING_TIME = "ml_training_time", "ML Training Time (s)"
        API_CALLS = "api_calls", "API Calls"
        DATASET_UPLOADS = "dataset_uploads", "Dataset Uploads"
        REPORT_GENERATIONS = "report_generations", "Report Generations"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    organization = models.ForeignKey(
        "accounts.Organization", on_delete=models.CASCADE, related_name="usage_records"
    )
    metric = models.CharField(max_length=30, choices=MetricChoices.choices)
    quantity = models.BigIntegerField(default=0)
    period_start = models.DateTimeField()
    period_end = models.DateTimeField()
    metadata = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["organization", "metric", "period_start"]),
        ]

    def __str__(self):
        return f"{self.organization.name} - {self.metric}: {self.quantity}"


class Invoice(models.Model):
    """Invoice records for billing history."""

    class StatusChoices(models.TextChoices):
        DRAFT = "draft", "Draft"
        OPEN = "open", "Open"
        PAID = "paid", "Paid"
        VOID = "void", "Void"
        UNCOLLECTIBLE = "uncollectible", "Uncollectible"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    organization = models.ForeignKey(
        "accounts.Organization", on_delete=models.CASCADE, related_name="invoices"
    )
    stripe_invoice_id = models.CharField(max_length=255, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default="usd")
    status = models.CharField(max_length=20, choices=StatusChoices.choices, default=StatusChoices.DRAFT)
    description = models.TextField(blank=True)
    period_start = models.DateTimeField()
    period_end = models.DateTimeField()
    paid_at = models.DateTimeField(null=True, blank=True)
    pdf_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Invoice {self.id} - {self.organization.name} - ${self.amount}"
