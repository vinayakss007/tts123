# DAaaS Platform - Data Analytics as a Service

A comprehensive SaaS platform that enables businesses to upload, clean, analyze, and visualize their data with AI-powered insights and automated machine learning.

## Overview

DAaaS (Data Analytics as a Service) is designed for small and medium businesses that need powerful data analytics capabilities without a dedicated data science team. The platform provides:

- **Data Upload & Management** - CSV, Excel, JSON, Parquet support with versioning
- **Data Cleaning** - AI-powered data quality fixes, deduplication, normalization
- **Statistical Analysis** - Descriptive stats, correlations, hypothesis testing
- **Data Visualization** - Interactive charts and dashboards
- **Machine Learning** - AutoML for classification, regression, clustering
- **AI-Powered Reports** - Natural language insights and automated report generation
- **Real-time Collaboration** - Multi-user workspaces with live updates

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Backend | Django 5.x + Django REST Framework |
| Frontend | React 18 + TypeScript + Vite |
| Database | PostgreSQL 16 + MongoDB 7 |
| Cache/Queue | Redis 7 + Celery |
| AI Gateway | OpenAI, Anthropic, Groq, Ollama |
| Storage | S3-compatible (MinIO for dev) |
| Deployment | Docker + Kubernetes |

## Prerequisites

- Docker & Docker Compose v2+
- Git
- Make (optional, for convenience commands)

## Quick Start

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd daaas-platform
   ```

2. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

3. **Start the development stack**
   ```bash
   make setup
   # Or manually:
   docker-compose up --build
   ```

4. **Access the application**
   - Frontend: http://localhost:5173
   - Backend API: http://localhost:8000/api/v1/
   - API Docs: http://localhost:8000/api/docs/
   - MinIO Console: http://localhost:9001

5. **Create a superuser**
   ```bash
   make createsuperuser
   ```

## Project Structure

```
daaas-platform/
├── backend/              # Django API application
│   ├── apps/            # Django applications
│   │   ├── accounts/    # User & organization management
│   │   ├── datasets/    # Data upload & storage
│   │   ├── analytics/   # Analysis & visualization
│   │   ├── ml_models/   # Machine learning
│   │   ├── reports/     # Report generation
│   │   ├── billing/     # Subscriptions & payments
│   │   ├── ai_gateway/  # Unified AI provider interface
│   │   └── notifications/ # Real-time notifications
│   ├── common/          # Shared utilities
│   ├── config/          # Django settings & configuration
│   └── tests/           # Test suite
├── frontend/            # React TypeScript application
│   └── src/
│       ├── components/  # UI components
│       ├── pages/       # Route pages
│       ├── hooks/       # Custom React hooks
│       ├── services/    # API services
│       ├── store/       # State management (Zustand)
│       └── types/       # TypeScript type definitions
├── infrastructure/      # DevOps & deployment
│   ├── kubernetes/      # K8s manifests
│   ├── terraform/       # Infrastructure as code
│   ├── monitoring/      # Prometheus & Grafana
│   └── nginx/           # Reverse proxy config
├── scripts/             # Utility scripts
├── docs/                # Documentation
└── .github/workflows/   # CI/CD pipelines
```

## Development

### Common Commands

```bash
make help           # Show all available commands
make up             # Start services
make down           # Stop services
make test           # Run backend tests
make lint           # Run linters
make format         # Format code
make migrate        # Run database migrations
make shell          # Django shell
```

### Running Tests

```bash
# Backend tests
make test
make test-cov       # With coverage

# Frontend tests
make test-frontend
```

### Code Quality

```bash
# Backend
make lint           # flake8 + mypy
make format         # black + isort

# Frontend
make lint-frontend
make format-frontend
```

## API Documentation

API documentation is available at `/api/docs/` when the backend is running. The API uses:

- RESTful design with versioned endpoints (`/api/v1/`)
- JWT authentication with refresh tokens
- Consistent error response format
- Cursor-based pagination for large datasets

## Architecture

The platform follows a modular architecture with:

- **Multi-tenant isolation** - Organization-based data separation
- **AI Gateway** - Single interface to multiple LLM providers with automatic fallback
- **Event-driven processing** - Celery for async tasks (ML training, report generation)
- **Real-time updates** - WebSocket notifications for long-running operations
- **Horizontal scaling** - Stateless backend designed for Kubernetes deployment

## Contributing

Please see [docs/architecture/README.md](docs/architecture/README.md) for architecture decisions and coding conventions.

## License

Proprietary - All rights reserved.
