export interface TrainingRun {
  id: string;
  status: 'queued' | 'running' | 'completed' | 'failed';
  hyperparameters: Record<string, unknown>;
  metrics: Record<string, number>;
  started_at?: string;
  completed_at?: string;
  duration_seconds?: number;
}

export interface MLModel {
  id: string;
  name: string;
  description: string;
  model_type: string;
  task_type: string;
  target_column: string;
  feature_columns: string[];
  status: 'draft' | 'training' | 'trained' | 'deployed' | 'error';
  dataset: string;
  created_at: string;
}
