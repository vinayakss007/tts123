import { Dataset } from '@/types/dataset';
import DataTable from '@/components/common/DataTable';

interface DatasetPreviewProps {
  dataset: Dataset;
  previewData?: Record<string, unknown>[];
}

export default function DatasetPreview({ dataset, previewData = [] }: DatasetPreviewProps) {
  if (!dataset.columns || dataset.columns.length === 0) {
    return <div className="text-center py-8 text-gray-500">No preview available</div>;
  }

  const columns = dataset.columns.map((col) => ({
    key: col.name as keyof Record<string, unknown>,
    header: `${col.name} (${col.data_type})`,
  }));

  return (
    <div className="space-y-4">
      <div className="flex items-center gap-4 text-sm text-gray-500">
        <span>{dataset.row_count?.toLocaleString()} rows</span>
        <span>{dataset.column_count} columns</span>
      </div>
      <DataTable columns={columns} data={previewData as any} emptyMessage="No preview data available" />
    </div>
  );
}
