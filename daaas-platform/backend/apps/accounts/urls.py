"""URL routing for accounts app."""
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import OrganizationViewSet, RegistrationViewSet, UserViewSet

router = DefaultRouter()
router.register(r"register", RegistrationViewSet, basename="register")
router.register(r"users", UserViewSet, basename="users")
router.register(r"organizations", OrganizationViewSet, basename="organizations")

urlpatterns = [
    path("", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
