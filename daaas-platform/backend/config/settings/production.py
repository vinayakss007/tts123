"""Production settings for DAaaS platform."""
from .base import *  # noqa: F401, F403

DEBUG = False

# Security settings
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = "DENY"
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Use cached template loader in production
TEMPLATES[0]["OPTIONS"]["loaders"] = [  # noqa: F405
    (
        "django.template.loaders.cached.Loader",
        [
            "django.template.loaders.filesystem.Loader",
            "django.template.loaders.app_directories.Loader",
        ],
    ),
]
TEMPLATES[0]["APP_DIRS"] = False  # noqa: F405

# Sentry error tracking
import sentry_sdk  # noqa: E402
from sentry_sdk.integrations.django import DjangoIntegration  # noqa: E402
from sentry_sdk.integrations.celery import CeleryIntegration  # noqa: E402

SENTRY_DSN = config("SENTRY_DSN", default="")  # noqa: F405
if SENTRY_DSN:
    sentry_sdk.init(
        dsn=SENTRY_DSN,
        integrations=[DjangoIntegration(), CeleryIntegration()],
        traces_sample_rate=0.1,
        send_default_pii=False,
    )
