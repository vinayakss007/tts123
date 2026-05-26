export const APP_NAME = 'DAaaS Platform';
export const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || '/api/v1';
export const WS_BASE_URL = import.meta.env.VITE_WS_BASE_URL || 'ws://localhost:8000/ws';

export const MAX_FILE_SIZE_MB = 500;
export const ALLOWED_FILE_TYPES = ['csv', 'xlsx', 'xls', 'json', 'parquet', 'tsv'];

export const CHART_COLORS = [
  '#3b82f6', '#10b981', '#f59e0b', '#ef4444',
  '#8b5cf6', '#06b6d4', '#f97316', '#ec4899',
];

export const PLAN_TIERS = {
  FREE: 'free',
  STARTER: 'starter',
  PROFESSIONAL: 'professional',
  ENTERPRISE: 'enterprise',
} as const;
