"""Stripe webhook handler for billing events."""
import stripe
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .models import Invoice, Subscription


@csrf_exempt
@require_POST
def stripe_webhook(request):
    """Handle incoming Stripe webhook events.

    Supported events:
    - customer.subscription.created
    - customer.subscription.updated
    - customer.subscription.deleted
    - invoice.paid
    - invoice.payment_failed
    """
    payload = request.body
    sig_header = request.META.get("HTTP_STRIPE_SIGNATURE")

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        return HttpResponse(status=400)

    event_type = event["type"]
    data = event["data"]["object"]

    if event_type == "customer.subscription.created":
        _handle_subscription_created(data)
    elif event_type == "customer.subscription.updated":
        _handle_subscription_updated(data)
    elif event_type == "customer.subscription.deleted":
        _handle_subscription_deleted(data)
    elif event_type == "invoice.paid":
        _handle_invoice_paid(data)
    elif event_type == "invoice.payment_failed":
        _handle_invoice_payment_failed(data)

    return HttpResponse(status=200)


def _handle_subscription_created(data: dict):
    """Handle new subscription creation from Stripe."""
    pass


def _handle_subscription_updated(data: dict):
    """Handle subscription updates (plan change, status change)."""
    stripe_sub_id = data.get("id")
    try:
        subscription = Subscription.objects.get(stripe_subscription_id=stripe_sub_id)
        subscription.status = data.get("status", subscription.status)
        subscription.save(update_fields=["status"])
    except Subscription.DoesNotExist:
        pass


def _handle_subscription_deleted(data: dict):
    """Handle subscription cancellation."""
    stripe_sub_id = data.get("id")
    try:
        subscription = Subscription.objects.get(stripe_subscription_id=stripe_sub_id)
        subscription.status = Subscription.StatusChoices.CANCELLED
        subscription.save(update_fields=["status"])
    except Subscription.DoesNotExist:
        pass


def _handle_invoice_paid(data: dict):
    """Handle successful invoice payment."""
    pass


def _handle_invoice_payment_failed(data: dict):
    """Handle failed invoice payment."""
    pass
