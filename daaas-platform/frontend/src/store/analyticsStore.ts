import { create } from 'zustand';

interface AnalyticsState {
  activeSessionId: string | null;
  results: Record<string, unknown>;
  setActiveSession: (id: string | null) => void;
  setResults: (results: Record<string, unknown>) => void;
}

export const useAnalyticsStore = create<AnalyticsState>((set) => ({
  activeSessionId: null,
  results: {},
  setActiveSession: (id) => set({ activeSessionId: id }),
  setResults: (results) => set({ results }),
}));
