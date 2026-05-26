# DAaaS Platform - Deployment Guide

## Environments

- **Development**: Docker Compose on local machine
- **Staging**: Kubernetes cluster (auto-deployed on merge to develop)
- **Production**: Kubernetes cluster (manual deployment with approvals)

## Prerequisites

- Docker and Docker Compose (development)
- kubectl configured for the target cluster
- AWS CLI configured for ECR/EKS access
- Terraform >= 1.5.0 (infrastructure changes)

## Development Deployment

```bash
cp .env.example .env
docker-compose up --build
```

## Production Deployment

1. Build and push images via CI/CD pipeline
2. Apply Kubernetes manifests:
   ```bash
   kubectl apply -f infrastructure/kubernetes/
   ```
3. Run migrations:
   ```bash
   ./scripts/migrate.sh production
   ```

## Infrastructure (Terraform)

```bash
cd infrastructure/terraform
terraform init
terraform plan
terraform apply
```

## Monitoring

- Prometheus: Scrapes metrics from all services
- Grafana: Dashboards at `monitoring.daaas.io`
- Sentry: Error tracking for backend and frontend
