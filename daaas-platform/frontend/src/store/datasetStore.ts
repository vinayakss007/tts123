import { create } from 'zustand';
import { Dataset } from '@/types/dataset';

interface DatasetState {
  datasets: Dataset[];
  selectedDataset: Dataset | null;
  setDatasets: (datasets: Dataset[]) => void;
  selectDataset: (dataset: Dataset | null) => void;
  addDataset: (dataset: Dataset) => void;
  removeDataset: (id: string) => void;
}

export const useDatasetStore = create<DatasetState>((set) => ({
  datasets: [],
  selectedDataset: null,
  setDatasets: (datasets) => set({ datasets }),
  selectDataset: (dataset) => set({ selectedDataset: dataset }),
  addDataset: (dataset) => set((state) => ({ datasets: [dataset, ...state.datasets] })),
  removeDataset: (id) => set((state) => ({ datasets: state.datasets.filter((d) => d.id !== id) })),
}));
