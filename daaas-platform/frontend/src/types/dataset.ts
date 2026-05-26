export interface DataColumn {
  id: string;
  name: string;
  data_type: string;
  nullable: boolean;
  null_count: number;
  unique_count: number;
  min_value?: string;
  max_value?: string;
  mean_value?: number;
  std_value?: number;
  sample_values: unknown[];
  position: number;
}

export interface Dataset {
  id: string;
  name: string;
  description: string;
  file_name: string;
  file_size: number;
  file_type: string;
  row_count: number | null;
  column_count: number | null;
  status: 'uploading' | 'processing' | 'ready' | 'error';
  tags: string[];
  columns: DataColumn[];
  created_at: string;
  updated_at: string;
}
