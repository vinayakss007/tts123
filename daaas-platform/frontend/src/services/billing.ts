import api from './api';

export const billingService = {
  async getPlans() {
    const { data } = await api.get('/billing/plans/');
    return data.results || data;
  },

  async getCurrentSubscription() {
    const { data } = await api.get('/billing/subscriptions/current/');
    return data;
  },

  async getUsage() {
    const { data } = await api.get('/billing/subscriptions/usage/');
    return data;
  },

  async createCheckout(planTier: string, interval: string = 'monthly') {
    const { data } = await api.post('/billing/subscriptions/checkout/', { plan_tier: planTier, billing_interval: interval });
    return data;
  },
};
