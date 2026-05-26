import { useState } from 'react';
import Button from '@/components/common/Button';

interface VisualizationBuilderProps {
  columns: string[];
  onCreateChart: (config: { chartType: string; xColumn: string; yColumn: string }) => void;
}

export default function VisualizationBuilder({ columns, onCreateChart }: VisualizationBuilderProps) {
  const [chartType, setChartType] = useState('bar');
  const [xColumn, setXColumn] = useState('');
  const [yColumn, setYColumn] = useState('');

  const handleCreate = () => {
    if (xColumn && yColumn) {
      onCreateChart({ chartType, xColumn, yColumn });
    }
  };

  return (
    <div className="card">
      <h3 className="font-medium mb-4">Create Visualization</h3>
      <div className="space-y-3">
        <div>
          <label className="text-sm text-gray-600">Chart Type</label>
          <select className="input-field text-sm mt-1" value={chartType} onChange={(e) => setChartType(e.target.value)}>
            <option value="bar">Bar Chart</option>
            <option value="line">Line Chart</option>
            <option value="scatter">Scatter Plot</option>
            <option value="pie">Pie Chart</option>
            <option value="histogram">Histogram</option>
          </select>
        </div>
        <div>
          <label className="text-sm text-gray-600">X Axis</label>
          <select className="input-field text-sm mt-1" value={xColumn} onChange={(e) => setXColumn(e.target.value)}>
            <option value="">Select column...</option>
            {columns.map((col) => <option key={col} value={col}>{col}</option>)}
          </select>
        </div>
        <div>
          <label className="text-sm text-gray-600">Y Axis</label>
          <select className="input-field text-sm mt-1" value={yColumn} onChange={(e) => setYColumn(e.target.value)}>
            <option value="">Select column...</option>
            {columns.map((col) => <option key={col} value={col}>{col}</option>)}
          </select>
        </div>
        <Button size="sm" onClick={handleCreate} className="w-full">Create Chart</Button>
      </div>
    </div>
  );
}
