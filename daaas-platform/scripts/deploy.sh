#!/bin/bash
# DAaaS Platform - Deployment Script
set -e

ENVIRONMENT=${1:-staging}
IMAGE_TAG=${2:-latest}

echo "=== Deploying DAaaS Platform ==="
echo "Environment: $ENVIRONMENT"
echo "Image Tag: $IMAGE_TAG"
echo ""

# Validate environment
if [[ "$ENVIRONMENT" != "staging" && "$ENVIRONMENT" != "production" ]]; then
    echo "Error: Environment must be 'staging' or 'production'"
    exit 1
fi

# Set namespace
NAMESPACE="daaas-${ENVIRONMENT}"

# Update deployments
echo "Updating backend deployment..."
kubectl set image deployment/daaas-backend backend=daaas/backend:${IMAGE_TAG} -n ${NAMESPACE}

echo "Updating frontend deployment..."
kubectl set image deployment/daaas-frontend frontend=daaas/frontend:${IMAGE_TAG} -n ${NAMESPACE}

echo "Updating celery worker..."
kubectl set image deployment/daaas-celery-worker celery-worker=daaas/backend:${IMAGE_TAG} -n ${NAMESPACE}

echo "Updating celery beat..."
kubectl set image deployment/daaas-celery-beat celery-beat=daaas/backend:${IMAGE_TAG} -n ${NAMESPACE}

# Wait for rollouts
echo "Waiting for rollouts to complete..."
kubectl rollout status deployment/daaas-backend -n ${NAMESPACE} --timeout=300s
kubectl rollout status deployment/daaas-frontend -n ${NAMESPACE} --timeout=300s
kubectl rollout status deployment/daaas-celery-worker -n ${NAMESPACE} --timeout=300s

echo ""
echo "=== Deployment Complete ==="
