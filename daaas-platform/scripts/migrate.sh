#!/bin/bash
# DAaaS Platform - Database Migration Script
set -e

ENVIRONMENT=${1:-development}

echo "=== Running Database Migrations ==="
echo "Environment: $ENVIRONMENT"
echo ""

if [ "$ENVIRONMENT" = "development" ]; then
    docker-compose exec -T backend python manage.py makemigrations
    docker-compose exec -T backend python manage.py migrate
elif [ "$ENVIRONMENT" = "production" ]; then
    NAMESPACE="daaas-production"
    POD=$(kubectl get pods -n ${NAMESPACE} -l app=daaas,component=backend -o jsonpath='{.items[0].metadata.name}')
    echo "Running migrations on pod: $POD"
    kubectl exec -n ${NAMESPACE} ${POD} -- python manage.py migrate --noinput
fi

echo ""
echo "=== Migrations Complete ==="
