"""Common model and view mixins."""
import uuid

from django.db import models


class TimestampMixin(models.Model):
    """Add created_at and updated_at fields to a model."""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UUIDMixin(models.Model):
    """Use UUID as primary key."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class OrganizationMixin(models.Model):
    """Add organization foreign key for multi-tenant models."""

    organization = models.ForeignKey(
        "accounts.Organization",
        on_delete=models.CASCADE,
        related_name="%(class)ss",
    )

    class Meta:
        abstract = True


class OrganizationFilterMixin:
    """Filter queryset by user's active organization."""

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_authenticated:
            return qs.filter(organization=self.request.user.last_active_organization)
        return qs.none()

    def perform_create(self, serializer):
        serializer.save(organization=self.request.user.last_active_organization)
