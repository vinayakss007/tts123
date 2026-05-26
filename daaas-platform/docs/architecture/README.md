# DAaaS Platform - Architecture Overview

## System Architecture

The DAaaS platform follows a microservice-inspired modular monolith architecture:

```
[Browser] -> [Nginx] -> [Django API] -> [PostgreSQL]
                    |-> [React SPA]     [MongoDB]
                                        [Redis]
                    [Celery Workers] -> [AI Gateway] -> [OpenAI/Anthropic/Groq/Ollama]
                                   |-> [S3/MinIO]
```

## Key Design Decisions

### 1. Modular Monolith (Backend)
- Single Django application with isolated apps
- Each app has its own models, views, serializers, and tasks
- Clean boundaries allow future microservice extraction

### 2. AI Gateway Pattern
- Single interface to multiple LLM providers
- Automatic fallback with health checking
- Token budget enforcement per organization
- Provider-agnostic streaming support

### 3. Multi-Tenancy
- Organization-based data isolation
- Row-level security via queryset filtering
- RBAC with roles: Owner, Admin, Analyst, Viewer

### 4. Event-Driven Processing
- Celery for all async operations (ML training, report generation)
- Separate queues for different workload types
- Redis for both caching and message brokering

### 5. Real-Time Updates
- Django Channels with WebSocket consumers
- Notifications pushed to connected clients immediately
- Used for: training progress, dataset processing status, collaboration

## Technology Choices

| Concern | Technology | Rationale |
|---------|-----------|-----------|
| API Framework | Django REST Framework | Mature, batteries-included, excellent DX |
| Frontend | React + TypeScript | Type safety, large ecosystem, Vite for fast dev |
| Primary DB | PostgreSQL | ACID compliance, JSON support, mature |
| Document Store | MongoDB | Flexible schema for analysis results |
| Cache/Queue | Redis | Fast, versatile, Celery integration |
| AI | Multi-provider gateway | Avoid vendor lock-in, cost optimization |
| Storage | S3-compatible | Industry standard, MinIO for local dev |
