"""Custom middleware for the DAaaS platform."""
import logging
import time
import uuid

from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger(__name__)


class RequestLoggingMiddleware(MiddlewareMixin):
    """Log request/response details for monitoring and debugging."""

    def process_request(self, request):
        """Add request ID and start time."""
        request.request_id = str(uuid.uuid4())
        request.start_time = time.time()

    def process_response(self, request, response):
        """Log request details with timing information."""
        if hasattr(request, "start_time"):
            duration = time.time() - request.start_time
            logger.info(
                "request_completed",
                extra={
                    "request_id": getattr(request, "request_id", ""),
                    "method": request.method,
                    "path": request.path,
                    "status_code": response.status_code,
                    "duration_ms": int(duration * 1000),
                    "user": str(request.user) if request.user.is_authenticated else "anonymous",
                },
            )

        response["X-Request-ID"] = getattr(request, "request_id", "")
        return response


class TenantMiddleware(MiddlewareMixin):
    """Set the active organization context for the request.

    Resolves the organization from the request header or user preference.
    """

    HEADER_NAME = "X-Organization-ID"

    def process_request(self, request):
        """Resolve and set the active organization for the request."""
        if not request.user.is_authenticated:
            return

        org_id = request.headers.get(self.HEADER_NAME)

        if org_id:
            from apps.accounts.models import Membership

            try:
                membership = Membership.objects.get(
                    user=request.user, organization_id=org_id
                )
                request.organization = membership.organization
            except Membership.DoesNotExist:
                request.organization = request.user.last_active_organization
        else:
            request.organization = request.user.last_active_organization
