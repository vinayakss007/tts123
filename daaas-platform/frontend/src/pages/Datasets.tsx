import { useState } from 'react';
import { Plus } from 'lucide-react';
import Button from '@/components/common/Button';
import DatasetUpload from '@/components/datasets/DatasetUpload';
import DatasetList from '@/components/datasets/DatasetList';
import Modal from '@/components/common/Modal';
import { useDatasets } from '@/hooks/useDatasets';

export default function Datasets() {
  const [showUpload, setShowUpload] = useState(false);
  const { datasets, upload, loading } = useDatasets();

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <h1 className="text-2xl font-bold">Datasets</h1>
        <Button onClick={() => setShowUpload(true)}>
          <Plus size={16} className="mr-2" /> Upload Dataset
        </Button>
      </div>
      <DatasetList datasets={datasets} onSelect={() => {}} />
      <Modal isOpen={showUpload} onClose={() => setShowUpload(false)} title="Upload Dataset" size="lg">
        <DatasetUpload onUpload={(file) => { upload(file); setShowUpload(false); }} loading={loading} />
      </Modal>
    </div>
  );
}
