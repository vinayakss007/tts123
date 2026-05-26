"""Serializers for user accounts and organization management."""
from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Invitation, Membership, Organization

User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    """Serializer for user registration."""

    password = serializers.CharField(write_only=True, min_length=8)
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "password", "password_confirm")

    def validate(self, data):
        if data["password"] != data["password_confirm"]:
            raise serializers.ValidationError({"password_confirm": "Passwords do not match."})
        return data

    def create(self, validated_data):
        validated_data.pop("password_confirm")
        return User.objects.create_user(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    """Serializer for user profile information."""

    class Meta:
        model = User
        fields = ("id", "email", "first_name", "last_name", "avatar", "is_email_verified", "date_joined")
        read_only_fields = ("id", "email", "is_email_verified", "date_joined")


class LoginSerializer(serializers.Serializer):
    """Serializer for user login."""

    email = serializers.EmailField()
    password = serializers.CharField()


class OrganizationSerializer(serializers.ModelSerializer):
    """Serializer for organization CRUD operations."""

    owner = UserSerializer(read_only=True)
    member_count = serializers.SerializerMethodField()

    class Meta:
        model = Organization
        fields = ("id", "name", "slug", "owner", "plan", "logo", "description", "member_count", "created_at")
        read_only_fields = ("id", "owner", "plan", "created_at")

    def get_member_count(self, obj):
        return obj.memberships.count()


class MembershipSerializer(serializers.ModelSerializer):
    """Serializer for organization membership."""

    user = UserSerializer(read_only=True)

    class Meta:
        model = Membership
        fields = ("id", "user", "organization", "role", "joined_at")
        read_only_fields = ("id", "joined_at")


class InvitationSerializer(serializers.ModelSerializer):
    """Serializer for organization invitations."""

    invited_by = UserSerializer(read_only=True)

    class Meta:
        model = Invitation
        fields = ("id", "email", "organization", "role", "invited_by", "status", "created_at", "expires_at")
        read_only_fields = ("id", "invited_by", "status", "created_at")
