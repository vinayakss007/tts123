import { BarChart3, Play } from 'lucide-react';
import Button from '@/components/common/Button';

interface AnalysisPanelProps {
  sessionId?: string;
  onRunAnalysis: () => void;
  loading?: boolean;
}

export default function AnalysisPanel({ sessionId, onRunAnalysis, loading }: AnalysisPanelProps) {
  return (
    <div className="card">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-2">
          <BarChart3 size={20} className="text-primary-600" />
          <h3 className="font-medium">Analysis</h3>
        </div>
        <Button size="sm" onClick={onRunAnalysis} loading={loading}>
          <Play size={14} className="mr-1" />
          Run Analysis
        </Button>
      </div>
      <div className="space-y-3">
        <select className="input-field text-sm">
          <option value="descriptive_stats">Descriptive Statistics</option>
          <option value="correlation">Correlation Analysis</option>
          <option value="distribution">Distribution Analysis</option>
          <option value="hypothesis_test">Hypothesis Test</option>
        </select>
      </div>
    </div>
  );
}
