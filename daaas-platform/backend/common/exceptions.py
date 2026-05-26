"""Custom exception handler for consistent API error responses."""
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    """Custom exception handler providing consistent error format.

    Response format:
    {
        "error": {
            "code": "ERROR_CODE",
            "message": "Human readable message",
            "details": {...}  // optional
        }
    }
    """
    response = exception_handler(exc, context)

    if response is not None:
        error_data = {
            "error": {
                "code": exc.__class__.__name__.upper(),
                "message": str(exc.detail) if hasattr(exc, "detail") else str(exc),
                "status_code": response.status_code,
            }
        }

        if isinstance(exc.detail, dict):
            error_data["error"]["details"] = exc.detail
        elif isinstance(exc.detail, list):
            error_data["error"]["details"] = exc.detail

        response.data = error_data

    return response


class ServiceUnavailableError(APIException):
    """Raised when an external service is unavailable."""

    status_code = status.HTTP_503_SERVICE_UNAVAILABLE
    default_detail = "Service temporarily unavailable. Please try again later."
    default_code = "service_unavailable"


class UsageLimitExceededError(APIException):
    """Raised when a usage limit is exceeded."""

    status_code = status.HTTP_429_TOO_MANY_REQUESTS
    default_detail = "Usage limit exceeded for your current plan."
    default_code = "usage_limit_exceeded"


class DataValidationError(APIException):
    """Raised when uploaded data fails validation."""

    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    default_detail = "Data validation failed."
    default_code = "data_validation_error"
