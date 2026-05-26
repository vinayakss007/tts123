"""Signals for the accounts app."""
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify

from .models import Membership, Organization, User


@receiver(post_save, sender=User)
def create_default_organization(sender, instance, created, **kwargs):
    """Create a default personal organization when a new user registers."""
    if created and not instance.is_superuser:
        org_name = f"{instance.first_name}'s Workspace"
        slug = slugify(f"{instance.first_name}-{instance.last_name}-{str(instance.id)[:8]}")

        org = Organization.objects.create(
            name=org_name,
            slug=slug,
            owner=instance,
        )
        Membership.objects.create(
            user=instance,
            organization=org,
            role=Membership.RoleChoices.OWNER,
        )
        instance.last_active_organization = org
        instance.save(update_fields=["last_active_organization"])
