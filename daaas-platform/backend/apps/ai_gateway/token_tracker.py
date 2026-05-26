"""Token usage counting and budget enforcement."""
import logging
from typing import Any

from django.conf import settings
from django.utils import timezone

logger = logging.getLogger(__name__)


class TokenTracker:
    """Track and enforce AI token usage budgets.

    Monitors token consumption per organization and enforces
    monthly limits based on subscription plan.
    """

    def __init__(self, organization=None):
        self.organization = organization

    def has_budget(self) -> bool:
        """Check if the organization has remaining token budget.

        Returns:
            True if within budget, False if exceeded.
        """
        if not self.organization:
            return True

        monthly_limit = self._get_monthly_limit()
        current_usage = self._get_current_usage()

        return current_usage < monthly_limit

    def record_usage(self, usage: dict[str, int]) -> None:
        """Record token usage from a completion response.

        Args:
            usage: Dictionary with prompt_tokens, completion_tokens, total_tokens.
        """
        if not self.organization:
            return

        from apps.billing.services import MeteringService
        from .models import AIUsageLog

        total_tokens = usage.get("total_tokens", 0)
        if total_tokens > 0:
            metering = MeteringService()
            metering.record_usage(
                organization=self.organization,
                metric="ai_tokens",
                quantity=total_tokens,
            )

    def get_remaining_budget(self) -> int:
        """Get remaining tokens for the current billing period."""
        monthly_limit = self._get_monthly_limit()
        current_usage = self._get_current_usage()
        return max(0, monthly_limit - current_usage)

    def get_usage_percentage(self) -> float:
        """Get current usage as a percentage of the monthly limit."""
        monthly_limit = self._get_monthly_limit()
        if monthly_limit == 0:
            return 100.0
        current_usage = self._get_current_usage()
        return (current_usage / monthly_limit) * 100

    def _get_monthly_limit(self) -> int:
        """Get the monthly token limit for the organization."""
        if not self.organization:
            return settings.AI_MONTHLY_TOKEN_BUDGET

        try:
            subscription = self.organization.subscription
            return subscription.plan.max_ai_tokens_monthly
        except Exception:
            return settings.AI_MONTHLY_TOKEN_BUDGET

    def _get_current_usage(self) -> int:
        """Get current month token usage from billing records."""
        from apps.billing.models import UsageRecord

        now = timezone.now()
        period_start = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)

        try:
            record = UsageRecord.objects.get(
                organization=self.organization,
                metric="ai_tokens",
                period_start=period_start,
            )
            return record.quantity
        except UsageRecord.DoesNotExist:
            return 0
