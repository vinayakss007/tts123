"""Billing metering and usage tracking service."""
from datetime import datetime
from typing import Any

from django.utils import timezone

from .models import UsageRecord


class MeteringService:
    """Track and report resource usage for billing."""

    def record_usage(self, organization, metric: str, quantity: int, metadata: dict = None):
        """Record a usage event for an organization.

        Args:
            organization: Organization instance
            metric: Usage metric type
            quantity: Amount to record
            metadata: Additional context data
        """
        now = timezone.now()
        period_start = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)

        if now.month == 12:
            period_end = period_start.replace(year=now.year + 1, month=1)
        else:
            period_end = period_start.replace(month=now.month + 1)

        record, created = UsageRecord.objects.get_or_create(
            organization=organization,
            metric=metric,
            period_start=period_start,
            period_end=period_end,
            defaults={"quantity": quantity, "metadata": metadata or {}},
        )
        if not created:
            record.quantity += quantity
            record.save(update_fields=["quantity"])

        return record

    def get_usage_summary(self, organization) -> dict[str, Any]:
        """Get current period usage summary for an organization."""
        now = timezone.now()
        period_start = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)

        records = UsageRecord.objects.filter(
            organization=organization,
            period_start=period_start,
        )

        summary = {}
        for record in records:
            summary[record.metric] = record.quantity

        return {
            "period_start": period_start.isoformat(),
            "usage": summary,
        }

    def check_limit(self, organization, metric: str, limit: int) -> bool:
        """Check if organization has exceeded a usage limit."""
        now = timezone.now()
        period_start = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)

        try:
            record = UsageRecord.objects.get(
                organization=organization,
                metric=metric,
                period_start=period_start,
            )
            return record.quantity < limit
        except UsageRecord.DoesNotExist:
            return True
