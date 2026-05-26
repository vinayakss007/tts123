"""URL routing for datasets app."""
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import DatasetViewSet, DataSourceViewSet

router = DefaultRouter()
router.register(r"datasets", DatasetViewSet, basename="datasets")
router.register(r"sources", DataSourceViewSet, basename="data-sources")

urlpatterns = [
    path("", include(router.urls)),
]
