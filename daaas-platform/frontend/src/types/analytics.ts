export interface AnalysisStep {
  id: string;
  step_type: string;
  order: number;
  parameters: Record<string, unknown>;
  result: Record<string, unknown>;
  status: 'pending' | 'running' | 'completed' | 'error';
  execution_time_ms?: number;
}

export interface AnalysisSession {
  id: string;
  name: string;
  description: string;
  dataset: string;
  status: 'draft' | 'running' | 'completed' | 'error';
  steps: AnalysisStep[];
  created_at: string;
}
