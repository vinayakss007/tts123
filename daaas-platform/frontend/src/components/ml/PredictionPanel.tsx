import { useState } from 'react';
import Button from '@/components/common/Button';

interface PredictionPanelProps {
  featureColumns: string[];
  onPredict: (inputData: Record<string, string>) => void;
  loading?: boolean;
  result?: unknown;
}

export default function PredictionPanel({ featureColumns, onPredict, loading, result }: PredictionPanelProps) {
  const [inputs, setInputs] = useState<Record<string, string>>({});

  const handlePredict = () => {
    onPredict(inputs);
  };

  return (
    <div className="card">
      <h3 className="font-medium mb-4">Make Prediction</h3>
      <div className="space-y-3">
        {featureColumns.map((col) => (
          <div key={col}>
            <label className="text-xs text-gray-500">{col}</label>
            <input
              className="input-field text-sm"
              value={inputs[col] || ''}
              onChange={(e) => setInputs({ ...inputs, [col]: e.target.value })}
            />
          </div>
        ))}
        <Button size="sm" className="w-full" onClick={handlePredict} loading={loading}>
          Predict
        </Button>
        {result && (
          <div className="mt-3 p-3 bg-green-50 rounded-lg text-sm text-green-800">
            <strong>Result:</strong> {JSON.stringify(result)}
          </div>
        )}
      </div>
    </div>
  );
}
