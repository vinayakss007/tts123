import PricingPlans from '@/components/billing/PricingPlans';
import UsageDashboard from '@/components/billing/UsageDashboard';

const samplePlans = [
  { name: 'Starter', tier: 'starter', price_monthly: 29, features: ['50 Datasets', '10 GB Storage', '100K AI Tokens'] },
  { name: 'Professional', tier: 'professional', price_monthly: 99, features: ['Unlimited Datasets', '100 GB Storage', '1M AI Tokens'] },
  { name: 'Enterprise', tier: 'enterprise', price_monthly: 299, features: ['Custom Limits', 'Priority Support', 'Custom Branding'] },
];

export default function Billing() {
  return (
    <div className="space-y-8">
      <h1 className="text-2xl font-bold">Billing & Subscription</h1>
      <UsageDashboard metrics={[
        { name: 'AI Tokens', used: 45000, limit: 100000, unit: 'tokens' },
        { name: 'Storage', used: 3, limit: 10, unit: 'GB' },
        { name: 'Datasets', used: 12, limit: 50, unit: '' },
      ]} />
      <PricingPlans plans={samplePlans} currentTier="starter" onSelectPlan={() => {}} />
    </div>
  );
}
