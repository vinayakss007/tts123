interface UsageMetric {
  name: string;
  used: number;
  limit: number;
  unit: string;
}

interface UsageDashboardProps {
  metrics: UsageMetric[];
}

export default function UsageDashboard({ metrics }: UsageDashboardProps) {
  return (
    <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
      {metrics.map((metric) => {
        const percentage = Math.min((metric.used / metric.limit) * 100, 100);
        return (
          <div key={metric.name} className="card">
            <h4 className="text-sm text-gray-500">{metric.name}</h4>
            <p className="text-xl font-bold mt-1">
              {metric.used.toLocaleString()} / {metric.limit.toLocaleString()}
              <span className="text-sm text-gray-400 ml-1">{metric.unit}</span>
            </p>
            <div className="mt-2 h-2 bg-gray-200 rounded-full overflow-hidden">
              <div
                className={`h-full rounded-full ${percentage > 90 ? 'bg-red-500' : percentage > 70 ? 'bg-yellow-500' : 'bg-green-500'}`}
                style={{ width: `${percentage}%` }}
              />
            </div>
          </div>
        );
      })}
    </div>
  );
}
