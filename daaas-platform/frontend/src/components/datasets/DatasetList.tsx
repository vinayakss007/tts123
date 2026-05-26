import { Database, Clock, FileType } from 'lucide-react';
import { Dataset } from '@/types/dataset';
import { formatFileSize, formatDate } from '@/utils/formatters';

interface DatasetListProps {
  datasets: Dataset[];
  onSelect: (dataset: Dataset) => void;
}

export default function DatasetList({ datasets, onSelect }: DatasetListProps) {
  if (datasets.length === 0) {
    return (
      <div className="text-center py-12">
        <Database className="mx-auto text-gray-300" size={48} />
        <p className="mt-4 text-gray-500">No datasets yet. Upload your first dataset to get started.</p>
      </div>
    );
  }

  return (
    <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
      {datasets.map((dataset) => (
        <div
          key={dataset.id}
          onClick={() => onSelect(dataset)}
          className="card cursor-pointer hover:shadow-md transition-shadow"
        >
          <div className="flex items-start justify-between">
            <h3 className="font-medium text-gray-900 truncate">{dataset.name}</h3>
            <span className={`text-xs px-2 py-1 rounded-full ${
              dataset.status === 'ready' ? 'bg-green-100 text-green-700' :
              dataset.status === 'processing' ? 'bg-yellow-100 text-yellow-700' :
              'bg-red-100 text-red-700'
            }`}>
              {dataset.status}
            </span>
          </div>
          <div className="mt-3 space-y-2 text-sm text-gray-500">
            <div className="flex items-center gap-2">
              <FileType size={14} />
              <span>{dataset.file_type.toUpperCase()} - {formatFileSize(dataset.file_size)}</span>
            </div>
            <div className="flex items-center gap-2">
              <Database size={14} />
              <span>{dataset.row_count?.toLocaleString()} rows, {dataset.column_count} columns</span>
            </div>
            <div className="flex items-center gap-2">
              <Clock size={14} />
              <span>{formatDate(dataset.created_at)}</span>
            </div>
          </div>
        </div>
      ))}
    </div>
  );
}
