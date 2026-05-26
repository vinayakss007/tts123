"""URL routing for billing app."""
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import InvoiceViewSet, PlanViewSet, SubscriptionViewSet
from .webhooks import stripe_webhook

router = DefaultRouter()
router.register(r"plans", PlanViewSet, basename="plans")
router.register(r"subscriptions", SubscriptionViewSet, basename="subscriptions")
router.register(r"invoices", InvoiceViewSet, basename="invoices")

urlpatterns = [
    path("", include(router.urls)),
    path("webhooks/stripe/", stripe_webhook, name="stripe-webhook"),
]
