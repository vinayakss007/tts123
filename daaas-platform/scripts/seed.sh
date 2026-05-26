#!/bin/bash
# DAaaS Platform - Database Seeding Script
set -e

echo "=== Seeding Database ==="
echo ""

# Create default plans
docker-compose exec -T backend python manage.py shell -c "
from apps.billing.models import Plan
from decimal import Decimal

plans = [
    {'name': 'Free', 'tier': 'free', 'price_monthly': Decimal('0'), 'price_yearly': Decimal('0'), 'max_datasets': 5, 'max_storage_gb': 1, 'max_ai_tokens_monthly': 10000, 'max_team_members': 1},
    {'name': 'Starter', 'tier': 'starter', 'price_monthly': Decimal('29'), 'price_yearly': Decimal('290'), 'max_datasets': 50, 'max_storage_gb': 10, 'max_ai_tokens_monthly': 100000, 'max_team_members': 5},
    {'name': 'Professional', 'tier': 'professional', 'price_monthly': Decimal('99'), 'price_yearly': Decimal('990'), 'max_datasets': 500, 'max_storage_gb': 100, 'max_ai_tokens_monthly': 1000000, 'max_team_members': 25, 'api_access': True},
    {'name': 'Enterprise', 'tier': 'enterprise', 'price_monthly': Decimal('299'), 'price_yearly': Decimal('2990'), 'max_datasets': 10000, 'max_storage_gb': 1000, 'max_ai_tokens_monthly': 10000000, 'max_team_members': 100, 'custom_branding': True, 'priority_support': True, 'api_access': True},
]

for plan_data in plans:
    Plan.objects.update_or_create(tier=plan_data['tier'], defaults=plan_data)

print(f'Created/updated {len(plans)} plans')
"

echo ""
echo "=== Seeding Complete ==="
