"""URL routing for reports app."""
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ReportTemplateViewSet, ReportViewSet

router = DefaultRouter()
router.register(r"reports", ReportViewSet, basename="reports")
router.register(r"templates", ReportTemplateViewSet, basename="report-templates")

urlpatterns = [
    path("", include(router.urls)),
]
