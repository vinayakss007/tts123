import { useState, useEffect } from 'react';
import { Dataset } from '@/types/dataset';
import { datasetsService } from '@/services/datasets';

export function useDatasets() {
  const [datasets, setDatasets] = useState<Dataset[]>([]);
  const [loading, setLoading] = useState(false);

  const fetchDatasets = async () => {
    setLoading(true);
    try {
      const data = await datasetsService.list();
      setDatasets(data);
    } finally {
      setLoading(false);
    }
  };

  const upload = async (file: File) => {
    setLoading(true);
    try {
      await datasetsService.upload(file);
      await fetchDatasets();
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => { fetchDatasets(); }, []);

  return { datasets, loading, upload, refresh: fetchDatasets };
}
