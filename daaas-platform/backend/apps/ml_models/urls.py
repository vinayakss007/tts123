"""URL routing for ml_models app."""
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import MLModelViewSet

router = DefaultRouter()
router.register(r"models", MLModelViewSet, basename="ml-models")

urlpatterns = [
    path("", include(router.urls)),
]
