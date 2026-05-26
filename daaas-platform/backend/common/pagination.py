"""Custom pagination classes for the API."""
from rest_framework.pagination import CursorPagination, PageNumberPagination


class StandardPagination(PageNumberPagination):
    """Standard page number based pagination."""

    page_size = 25
    page_size_query_param = "page_size"
    max_page_size = 100


class LargeResultsPagination(PageNumberPagination):
    """Pagination for endpoints returning large datasets."""

    page_size = 100
    page_size_query_param = "page_size"
    max_page_size = 1000


class CursorBasedPagination(CursorPagination):
    """Cursor-based pagination for infinite scrolling and real-time data."""

    page_size = 50
    ordering = "-created_at"
    page_size_query_param = "page_size"
    max_page_size = 200
