import { useState } from 'react';
import Button from '@/components/common/Button';

interface ModelBuilderProps {
  columns: string[];
  onCreateModel: (config: { name: string; taskType: string; targetColumn: string; modelType: string }) => void;
}

export default function ModelBuilder({ columns, onCreateModel }: ModelBuilderProps) {
  const [name, setName] = useState('');
  const [taskType, setTaskType] = useState('classification');
  const [targetColumn, setTargetColumn] = useState('');
  const [modelType, setModelType] = useState('auto');

  return (
    <div className="card">
      <h3 className="font-medium mb-4">Build ML Model</h3>
      <div className="space-y-3">
        <input className="input-field text-sm" placeholder="Model name" value={name} onChange={(e) => setName(e.target.value)} />
        <select className="input-field text-sm" value={taskType} onChange={(e) => setTaskType(e.target.value)}>
          <option value="classification">Classification</option>
          <option value="regression">Regression</option>
          <option value="clustering">Clustering</option>
        </select>
        <select className="input-field text-sm" value={targetColumn} onChange={(e) => setTargetColumn(e.target.value)}>
          <option value="">Select target column...</option>
          {columns.map((col) => <option key={col} value={col}>{col}</option>)}
        </select>
        <select className="input-field text-sm" value={modelType} onChange={(e) => setModelType(e.target.value)}>
          <option value="auto">Auto (Best Model)</option>
          <option value="random_forest">Random Forest</option>
          <option value="gradient_boosting">Gradient Boosting</option>
          <option value="linear_regression">Linear Regression</option>
          <option value="svm">SVM</option>
        </select>
        <Button size="sm" className="w-full" onClick={() => onCreateModel({ name, taskType, targetColumn, modelType })}>
          Create Model
        </Button>
      </div>
    </div>
  );
}
