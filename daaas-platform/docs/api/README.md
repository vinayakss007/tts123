# DAaaS Platform - API Documentation

## Overview

The DAaaS API is a RESTful API built with Django REST Framework. All endpoints are versioned under `/api/v1/`.

## Authentication

All API requests (except registration and login) require a valid JWT token in the Authorization header:

```
Authorization: Bearer <access_token>
```

## Base URL

- Development: `http://localhost:8000/api/v1/`
- Production: `https://api.daaas.io/api/v1/`

## Endpoint Groups

| Group | Base Path | Description |
|-------|-----------|-------------|
| Accounts | `/api/v1/accounts/` | User registration, auth, organizations |
| Datasets | `/api/v1/datasets/` | Dataset upload, management, sources |
| Analytics | `/api/v1/analytics/` | Analysis sessions, cleaning, visualization |
| ML Models | `/api/v1/ml/` | Model training, prediction, versions |
| Reports | `/api/v1/reports/` | AI-powered report generation |
| Billing | `/api/v1/billing/` | Plans, subscriptions, usage |
| AI Gateway | `/api/v1/ai/` | AI completions and streaming |
| Notifications | `/api/v1/notifications/` | User notifications |

## Interactive Documentation

When the backend is running, visit:
- Swagger UI: `/api/docs/`
- ReDoc: `/api/redoc/`
