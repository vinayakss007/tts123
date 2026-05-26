"""Root URL configuration for DAaaS platform."""
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),
    # API v1
    path("api/v1/accounts/", include("apps.accounts.urls")),
    path("api/v1/datasets/", include("apps.datasets.urls")),
    path("api/v1/analytics/", include("apps.analytics.urls")),
    path("api/v1/ml/", include("apps.ml_models.urls")),
    path("api/v1/reports/", include("apps.reports.urls")),
    path("api/v1/billing/", include("apps.billing.urls")),
    path("api/v1/ai/", include("apps.ai_gateway.urls")),
    path("api/v1/notifications/", include("apps.notifications.urls")),
    # API Documentation
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    # Health check
    path("health/", include("health_check.urls")),
]
