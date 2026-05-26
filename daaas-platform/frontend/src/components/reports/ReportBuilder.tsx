import { useState } from 'react';
import Button from '@/components/common/Button';
import { FileText } from 'lucide-react';

interface ReportBuilderProps {
  datasets: { id: string; name: string }[];
  onGenerate: (config: { title: string; datasetId: string; format: string; instructions: string }) => void;
  loading?: boolean;
}

export default function ReportBuilder({ datasets, onGenerate, loading }: ReportBuilderProps) {
  const [title, setTitle] = useState('');
  const [datasetId, setDatasetId] = useState('');
  const [format, setFormat] = useState('html');
  const [instructions, setInstructions] = useState('');

  return (
    <div className="card">
      <div className="flex items-center gap-2 mb-4">
        <FileText size={20} className="text-primary-600" />
        <h3 className="font-medium">Generate Report</h3>
      </div>
      <div className="space-y-3">
        <input className="input-field" placeholder="Report title" value={title} onChange={(e) => setTitle(e.target.value)} />
        <select className="input-field" value={datasetId} onChange={(e) => setDatasetId(e.target.value)}>
          <option value="">Select dataset...</option>
          {datasets.map((d) => <option key={d.id} value={d.id}>{d.name}</option>)}
        </select>
        <select className="input-field" value={format} onChange={(e) => setFormat(e.target.value)}>
          <option value="html">HTML</option>
          <option value="pdf">PDF</option>
          <option value="markdown">Markdown</option>
        </select>
        <textarea
          className="input-field"
          rows={3}
          placeholder="Custom instructions (optional)"
          value={instructions}
          onChange={(e) => setInstructions(e.target.value)}
        />
        <Button className="w-full" onClick={() => onGenerate({ title, datasetId, format, instructions })} loading={loading}>
          Generate AI Report
        </Button>
      </div>
    </div>
  );
}
