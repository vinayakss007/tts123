"""ViewSets for billing and subscription management."""
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Invoice, Plan, Subscription, UsageRecord
from .serializers import (
    CreateCheckoutSerializer,
    InvoiceSerializer,
    PlanSerializer,
    SubscriptionSerializer,
    UsageRecordSerializer,
)
from .services import MeteringService


class PlanViewSet(viewsets.ReadOnlyModelViewSet):
    """List available subscription plans."""

    queryset = Plan.objects.filter(is_active=True)
    serializer_class = PlanSerializer
    permission_classes = [permissions.AllowAny]


class SubscriptionViewSet(viewsets.GenericViewSet):
    """Manage organization subscription."""

    serializer_class = SubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Subscription.objects.filter(
            organization=self.request.user.last_active_organization
        )

    @action(detail=False, methods=["get"])
    def current(self, request):
        """Get current subscription details."""
        subscription = self.get_queryset().first()
        if not subscription:
            return Response({"detail": "No active subscription"}, status=status.HTTP_404_NOT_FOUND)
        return Response(SubscriptionSerializer(subscription).data)

    @action(detail=False, methods=["post"])
    def checkout(self, request):
        """Create a Stripe checkout session for subscription."""
        serializer = CreateCheckoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # Stripe checkout session creation would happen here
        return Response({"checkout_url": ""}, status=status.HTTP_200_OK)

    @action(detail=False, methods=["post"])
    def cancel(self, request):
        """Cancel the current subscription."""
        subscription = self.get_queryset().first()
        if subscription:
            subscription.status = Subscription.StatusChoices.CANCELLED
            subscription.save(update_fields=["status"])
        return Response({"status": "cancelled"})

    @action(detail=False, methods=["get"])
    def usage(self, request):
        """Get current period usage summary."""
        org = request.user.last_active_organization
        service = MeteringService()
        usage_summary = service.get_usage_summary(org)
        return Response(usage_summary)


class InvoiceViewSet(viewsets.ReadOnlyModelViewSet):
    """List billing invoices."""

    serializer_class = InvoiceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Invoice.objects.filter(
            organization=self.request.user.last_active_organization
        )
