import AnalysisPanel from '@/components/analytics/AnalysisPanel';
import CleaningPanel from '@/components/analytics/CleaningPanel';
import VisualizationBuilder from '@/components/analytics/VisualizationBuilder';

export default function Analytics() {
  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold">Analytics</h1>
      <div className="grid gap-6 lg:grid-cols-3">
        <div className="lg:col-span-2 space-y-4">
          <AnalysisPanel onRunAnalysis={() => {}} />
          <VisualizationBuilder columns={[]} onCreateChart={() => {}} />
        </div>
        <div>
          <CleaningPanel onApplyOperation={() => {}} />
        </div>
      </div>
    </div>
  );
}
