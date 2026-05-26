import Button from '@/components/common/Button';
import { Check } from 'lucide-react';

interface Plan {
  name: string;
  tier: string;
  price_monthly: number;
  features: string[];
}

interface PricingPlansProps {
  plans: Plan[];
  currentTier?: string;
  onSelectPlan: (tier: string) => void;
}

export default function PricingPlans({ plans, currentTier, onSelectPlan }: PricingPlansProps) {
  return (
    <div className="grid gap-6 md:grid-cols-3">
      {plans.map((plan) => (
        <div key={plan.tier} className={`card ${plan.tier === currentTier ? 'ring-2 ring-primary-500' : ''}`}>
          <h3 className="text-lg font-bold">{plan.name}</h3>
          <p className="text-3xl font-bold mt-2">${plan.price_monthly}<span className="text-sm text-gray-500">/mo</span></p>
          <ul className="mt-4 space-y-2">
            {plan.features.map((f, i) => (
              <li key={i} className="flex items-center gap-2 text-sm">
                <Check size={14} className="text-green-500" />{f}
              </li>
            ))}
          </ul>
          <Button
            className="w-full mt-6"
            variant={plan.tier === currentTier ? 'secondary' : 'primary'}
            onClick={() => onSelectPlan(plan.tier)}
          >
            {plan.tier === currentTier ? 'Current Plan' : 'Upgrade'}
          </Button>
        </div>
      ))}
    </div>
  );
}
