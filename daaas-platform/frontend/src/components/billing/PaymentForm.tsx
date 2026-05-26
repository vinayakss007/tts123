import Button from '@/components/common/Button';

interface PaymentFormProps {
  onSubmit: () => void;
  loading?: boolean;
}

export default function PaymentForm({ onSubmit, loading }: PaymentFormProps) {
  return (
    <div className="card max-w-md">
      <h3 className="font-medium mb-4">Payment Details</h3>
      <p className="text-sm text-gray-500 mb-4">
        You will be redirected to Stripe for secure payment processing.
      </p>
      <Button className="w-full" onClick={onSubmit} loading={loading}>
        Proceed to Payment
      </Button>
    </div>
  );
}
