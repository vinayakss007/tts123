# =============================================================================
# DAaaS Platform - Backend Dockerfile
# =============================================================================

# ---------------------------------------------------------------------------
# Base stage
# ---------------------------------------------------------------------------
FROM python:3.12-slim as base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# ---------------------------------------------------------------------------
# Development stage
# ---------------------------------------------------------------------------
FROM base as development

COPY requirements.txt requirements-dev.txt ./
RUN pip install -r requirements-dev.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# ---------------------------------------------------------------------------
# Production stage
# ---------------------------------------------------------------------------
FROM base as production

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput 2>/dev/null || true

# Create non-root user
RUN addgroup --system django && adduser --system --ingroup django django
USER django

EXPOSE 8000

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "4", "--threads", "2"]
