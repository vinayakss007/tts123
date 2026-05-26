import Button from '@/components/common/Button';
import { Sparkles } from 'lucide-react';

interface CleaningPanelProps {
  onApplyOperation: (operation: string, params: Record<string, unknown>) => void;
  loading?: boolean;
}

export default function CleaningPanel({ onApplyOperation, loading }: CleaningPanelProps) {
  return (
    <div className="card">
      <div className="flex items-center gap-2 mb-4">
        <Sparkles size={20} className="text-primary-600" />
        <h3 className="font-medium">Data Cleaning</h3>
      </div>
      <div className="space-y-3">
        <Button
          variant="secondary"
          size="sm"
          className="w-full justify-start"
          onClick={() => onApplyOperation('remove_duplicates', {})}
          loading={loading}
        >
          Remove Duplicates
        </Button>
        <Button
          variant="secondary"
          size="sm"
          className="w-full justify-start"
          onClick={() => onApplyOperation('fill_missing', { strategy: 'mean' })}
          loading={loading}
        >
          Fill Missing Values
        </Button>
        <Button
          variant="secondary"
          size="sm"
          className="w-full justify-start"
          onClick={() => onApplyOperation('remove_outliers', { method: 'iqr' })}
          loading={loading}
        >
          Remove Outliers
        </Button>
        <Button
          variant="secondary"
          size="sm"
          className="w-full justify-start"
          onClick={() => onApplyOperation('normalize', {})}
          loading={loading}
        >
          Normalize
        </Button>
      </div>
    </div>
  );
}
