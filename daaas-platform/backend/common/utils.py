"""General utility functions shared across the application."""
import hashlib
import uuid
from datetime import datetime
from typing import Any


def generate_unique_slug(base: str, max_length: int = 100) -> str:
    """Generate a unique slug by appending a short UUID."""
    from django.utils.text import slugify

    slug = slugify(base)[:max_length - 9]
    return f"{slug}-{uuid.uuid4().hex[:8]}"


def file_hash(content: bytes) -> str:
    """Generate SHA-256 hash for file content."""
    return hashlib.sha256(content).hexdigest()


def format_file_size(size_bytes: int) -> str:
    """Format file size in human-readable format."""
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.1f} PB"


def truncate_string(s: str, max_length: int = 100, suffix: str = "...") -> str:
    """Truncate a string to max_length, adding suffix if truncated."""
    if len(s) <= max_length:
        return s
    return s[: max_length - len(suffix)] + suffix


def deep_merge(base: dict, override: dict) -> dict:
    """Deep merge two dictionaries, with override taking precedence."""
    result = base.copy()
    for key, value in override.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result
