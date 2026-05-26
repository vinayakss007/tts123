"""Django settings module selector.

Automatically selects the appropriate settings based on DJANGO_ENV environment variable.
"""
import os

env = os.environ.get("DJANGO_ENV", "development")

if env == "production":
    from .production import *  # noqa: F401, F403
elif env == "testing":
    from .testing import *  # noqa: F401, F403
else:
    from .development import *  # noqa: F401, F403
