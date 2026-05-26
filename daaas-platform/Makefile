.PHONY: help build up down restart logs shell migrate makemigrations test lint format seed setup clean

# Default target
help: ## Show this help message
	@echo "DAaaS Platform - Available Commands:"
	@echo "======================================"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

# ---------------------------------------------------------------------------
# Docker Commands
# ---------------------------------------------------------------------------
build: ## Build all Docker containers
	docker-compose build

up: ## Start all services in background
	docker-compose up -d

down: ## Stop all services
	docker-compose down

restart: ## Restart all services
	docker-compose restart

logs: ## Follow logs for all services
	docker-compose logs -f

logs-backend: ## Follow backend logs
	docker-compose logs -f backend

logs-celery: ## Follow celery worker logs
	docker-compose logs -f celery-worker

# ---------------------------------------------------------------------------
# Backend Commands
# ---------------------------------------------------------------------------
shell: ## Open Django shell in backend container
	docker-compose exec backend python manage.py shell_plus

bash: ## Open bash in backend container
	docker-compose exec backend bash

migrate: ## Run database migrations
	docker-compose exec backend python manage.py migrate

makemigrations: ## Create new migrations
	docker-compose exec backend python manage.py makemigrations

createsuperuser: ## Create Django superuser
	docker-compose exec backend python manage.py createsuperuser

collectstatic: ## Collect static files
	docker-compose exec backend python manage.py collectstatic --noinput

# ---------------------------------------------------------------------------
# Testing
# ---------------------------------------------------------------------------
test: ## Run all backend tests
	docker-compose exec backend pytest -v

test-cov: ## Run tests with coverage report
	docker-compose exec backend pytest --cov=apps --cov-report=html --cov-report=term-missing

test-fast: ## Run tests without slow markers
	docker-compose exec backend pytest -v -m "not slow"

test-frontend: ## Run frontend tests
	docker-compose exec frontend npm test

# ---------------------------------------------------------------------------
# Code Quality
# ---------------------------------------------------------------------------
lint: ## Run linters (flake8, mypy)
	docker-compose exec backend flake8 .
	docker-compose exec backend mypy apps/

format: ## Format code with black and isort
	docker-compose exec backend black .
	docker-compose exec backend isort .

lint-frontend: ## Lint frontend code
	docker-compose exec frontend npm run lint

format-frontend: ## Format frontend code
	docker-compose exec frontend npm run format

# ---------------------------------------------------------------------------
# Database
# ---------------------------------------------------------------------------
seed: ## Seed database with sample data
	docker-compose exec backend python manage.py loaddata fixtures/*.json

db-reset: ## Reset database (WARNING: destroys all data)
	docker-compose exec backend python manage.py flush --noinput
	docker-compose exec backend python manage.py migrate
	docker-compose exec backend python manage.py createsuperuser

db-dump: ## Dump database to file
	docker-compose exec postgres pg_dump -U $${POSTGRES_USER:-daaas_user} $${POSTGRES_DB:-daaas} > backup.sql

# ---------------------------------------------------------------------------
# Setup & Utilities
# ---------------------------------------------------------------------------
setup: ## Initial project setup
	cp -n .env.example .env || true
	cp -n frontend/.env.example frontend/.env || true
	docker-compose build
	docker-compose up -d postgres redis mongo
	sleep 5
	docker-compose up -d
	docker-compose exec backend python manage.py migrate
	@echo "Setup complete! Access the app at http://localhost:5173"

clean: ## Remove all containers, volumes, and built images
	docker-compose down -v --rmi local
	rm -rf backend/staticfiles
	rm -rf frontend/node_modules frontend/dist

# ---------------------------------------------------------------------------
# Production
# ---------------------------------------------------------------------------
prod-build: ## Build production images
	docker-compose -f docker-compose.prod.yml build

prod-up: ## Start production stack
	docker-compose -f docker-compose.prod.yml up -d

prod-down: ## Stop production stack
	docker-compose -f docker-compose.prod.yml down
