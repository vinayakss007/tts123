#!/bin/bash
# DAaaS Platform - Local Development Setup Script
set -e

echo "=== DAaaS Platform Setup ==="
echo ""

# Check prerequisites
command -v docker >/dev/null 2>&1 || { echo "Docker is required but not installed. Aborting."; exit 1; }
command -v docker-compose >/dev/null 2>&1 || command -v "docker compose" >/dev/null 2>&1 || { echo "Docker Compose is required but not installed. Aborting."; exit 1; }

# Copy environment files
echo "Setting up environment files..."
cp -n .env.example .env 2>/dev/null || true
cp -n frontend/.env.example frontend/.env 2>/dev/null || true

# Build containers
echo "Building Docker containers..."
docker-compose build

# Start infrastructure services first
echo "Starting infrastructure services..."
docker-compose up -d postgres redis mongo minio

# Wait for services to be healthy
echo "Waiting for services to be ready..."
sleep 10

# Start application services
echo "Starting application services..."
docker-compose up -d

# Run migrations
echo "Running database migrations..."
docker-compose exec -T backend python manage.py migrate

echo ""
echo "=== Setup Complete ==="
echo ""
echo "Frontend: http://localhost:5173"
echo "Backend API: http://localhost:8000/api/v1/"
echo "API Docs: http://localhost:8000/api/docs/"
echo "MinIO Console: http://localhost:9001"
echo ""
echo "Run 'make createsuperuser' to create an admin account."
