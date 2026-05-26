interface TrainingProgressProps {
  status: string;
  progress?: number;
  metrics?: Record<string, number>;
}

export default function TrainingProgress({ status, progress, metrics }: TrainingProgressProps) {
  return (
    <div className="card">
      <h3 className="font-medium mb-3">Training Progress</h3>
      <div className="space-y-3">
        <div className="flex items-center justify-between text-sm">
          <span className="text-gray-600">Status</span>
          <span className={`font-medium ${status === 'completed' ? 'text-green-600' : status === 'running' ? 'text-blue-600' : 'text-gray-600'}`}>
            {status}
          </span>
        </div>
        {progress !== undefined && (
          <div>
            <div className="h-2 bg-gray-200 rounded-full overflow-hidden">
              <div className="h-full bg-primary-600 rounded-full transition-all" style={{ width: `${progress}%` }} />
            </div>
            <span className="text-xs text-gray-500 mt-1">{progress}%</span>
          </div>
        )}
        {metrics && Object.keys(metrics).length > 0 && (
          <div className="border-t pt-3 space-y-2">
            {Object.entries(metrics).map(([key, value]) => (
              <div key={key} className="flex items-center justify-between text-sm">
                <span className="text-gray-500 capitalize">{key.replace('_', ' ')}</span>
                <span className="font-mono">{typeof value === 'number' ? value.toFixed(4) : value}</span>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}
