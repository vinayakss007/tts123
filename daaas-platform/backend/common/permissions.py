"""Base permission classes for the API."""
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Allow write access only to the object owner."""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.created_by == request.user


class HasActiveSubscription(permissions.BasePermission):
    """Restrict access to users with an active subscription."""

    message = "An active subscription is required to access this resource."

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        org = request.user.last_active_organization
        if not org:
            return False

        try:
            subscription = org.subscription
            return subscription.status in ("active", "trialing")
        except Exception:
            return False


class HasPlanFeature(permissions.BasePermission):
    """Check if user's plan includes a specific feature."""

    required_feature = None  # Override in subclass

    def has_permission(self, request, view):
        if not self.required_feature:
            return True

        org = request.user.last_active_organization
        if not org:
            return False

        try:
            plan = org.subscription.plan
            return getattr(plan, self.required_feature, False)
        except Exception:
            return False
