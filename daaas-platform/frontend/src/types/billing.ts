export interface Plan {
  id: string;
  name: string;
  tier: string;
  price_monthly: number;
  price_yearly: number;
  max_datasets: number;
  max_storage_gb: number;
  max_ai_tokens_monthly: number;
  max_team_members: number;
}

export interface Subscription {
  id: string;
  plan: Plan;
  status: 'active' | 'trialing' | 'past_due' | 'cancelled';
  billing_interval: 'monthly' | 'yearly';
  current_period_end: string;
}
