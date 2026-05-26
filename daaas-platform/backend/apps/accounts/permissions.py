"""Custom permissions for organization-based access control."""
from rest_framework import permissions

from .models import Membership


class IsOrgMember(permissions.BasePermission):
    """Allow access if user is a member of the organization."""

    def has_object_permission(self, request, view, obj):
        return Membership.objects.filter(
            user=request.user,
            organization=obj,
        ).exists()


class IsOrgAdmin(permissions.BasePermission):
    """Allow access if user is an admin or owner of the organization."""

    def has_object_permission(self, request, view, obj):
        return Membership.objects.filter(
            user=request.user,
            organization=obj,
            role__in=[Membership.RoleChoices.ADMIN, Membership.RoleChoices.OWNER],
        ).exists()


class IsOrgOwner(permissions.BasePermission):
    """Allow access only if user is the owner of the organization."""

    def has_object_permission(self, request, view, obj):
        return Membership.objects.filter(
            user=request.user,
            organization=obj,
            role=Membership.RoleChoices.OWNER,
        ).exists()
