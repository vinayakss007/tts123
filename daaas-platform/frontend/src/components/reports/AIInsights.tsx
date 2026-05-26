import { Sparkles } from 'lucide-react';

interface AIInsightsProps {
  insights: string[];
  loading?: boolean;
}

export default function AIInsights({ insights, loading }: AIInsightsProps) {
  if (loading) {
    return (
      <div className="card animate-pulse">
        <div className="h-4 bg-gray-200 rounded w-1/3 mb-4" />
        <div className="space-y-2">
          <div className="h-3 bg-gray-200 rounded" />
          <div className="h-3 bg-gray-200 rounded w-5/6" />
        </div>
      </div>
    );
  }

  return (
    <div className="card">
      <div className="flex items-center gap-2 mb-4">
        <Sparkles size={18} className="text-primary-600" />
        <h3 className="font-medium">AI Insights</h3>
      </div>
      <ul className="space-y-2">
        {insights.map((insight, idx) => (
          <li key={idx} className="text-sm text-gray-600 pl-4 border-l-2 border-primary-200">
            {insight}
          </li>
        ))}
      </ul>
    </div>
  );
}
