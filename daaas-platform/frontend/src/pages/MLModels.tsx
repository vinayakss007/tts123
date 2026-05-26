import ModelBuilder from '@/components/ml/ModelBuilder';
import TrainingProgress from '@/components/ml/TrainingProgress';

export default function MLModels() {
  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold">Machine Learning Models</h1>
      <div className="grid gap-6 lg:grid-cols-3">
        <div className="lg:col-span-2">
          <div className="card">
            <p className="text-gray-500">Select a dataset and configure your ML model to get started.</p>
          </div>
        </div>
        <div className="space-y-4">
          <ModelBuilder columns={[]} onCreateModel={() => {}} />
          <TrainingProgress status="idle" />
        </div>
      </div>
    </div>
  );
}
