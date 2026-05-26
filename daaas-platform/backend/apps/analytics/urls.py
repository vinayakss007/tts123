"""URL routing for analytics app."""
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AnalysisSessionViewSet, CleaningOperationViewSet, VisualizationViewSet

router = DefaultRouter()
router.register(r"sessions", AnalysisSessionViewSet, basename="analysis-sessions")
router.register(r"visualizations", VisualizationViewSet, basename="visualizations")
router.register(r"cleaning", CleaningOperationViewSet, basename="cleaning-operations")

urlpatterns = [
    path("", include(router.urls)),
]
