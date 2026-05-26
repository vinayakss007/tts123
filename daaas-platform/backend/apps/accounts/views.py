"""ViewSets for user accounts and organization management."""
from django.contrib.auth import get_user_model
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Invitation, Membership, Organization
from .permissions import IsOrgAdmin, IsOrgMember, IsOrgOwner
from .serializers import (
    InvitationSerializer,
    MembershipSerializer,
    OrganizationSerializer,
    UserRegistrationSerializer,
    UserSerializer,
)

User = get_user_model()


class RegistrationViewSet(viewsets.GenericViewSet):
    """Handle user registration."""

    permission_classes = [permissions.AllowAny]
    serializer_class = UserRegistrationSerializer

    def create(self, request):
        """Register a new user and return tokens."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        refresh = RefreshToken.for_user(user)
        return Response(
            {
                "user": UserSerializer(user).data,
                "tokens": {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                },
            },
            status=status.HTTP_201_CREATED,
        )


class UserViewSet(viewsets.ModelViewSet):
    """Manage user profile."""

    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

    @action(detail=False, methods=["get", "patch"])
    def me(self, request):
        """Get or update current user profile."""
        if request.method == "GET":
            serializer = self.get_serializer(request.user)
            return Response(serializer.data)

        serializer = self.get_serializer(request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class OrganizationViewSet(viewsets.ModelViewSet):
    """Manage organizations."""

    serializer_class = OrganizationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Organization.objects.filter(members=self.request.user)

    def perform_create(self, serializer):
        org = serializer.save(owner=self.request.user)
        Membership.objects.create(
            user=self.request.user,
            organization=org,
            role=Membership.RoleChoices.OWNER,
        )

    @action(detail=True, methods=["get"], permission_classes=[IsOrgMember])
    def members(self, request, pk=None):
        """List organization members."""
        org = self.get_object()
        memberships = org.memberships.select_related("user").all()
        serializer = MembershipSerializer(memberships, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["post"], permission_classes=[IsOrgAdmin])
    def invite(self, request, pk=None):
        """Invite a user to the organization."""
        org = self.get_object()
        serializer = InvitationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(organization=org, invited_by=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=["delete"], permission_classes=[IsOrgOwner])
    def remove_member(self, request, pk=None):
        """Remove a member from the organization."""
        org = self.get_object()
        user_id = request.data.get("user_id")
        Membership.objects.filter(user_id=user_id, organization=org).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
