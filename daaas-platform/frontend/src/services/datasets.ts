import api from './api';
import { Dataset } from '@/types/dataset';

export const datasetsService = {
  async list(): Promise<Dataset[]> {
    const { data } = await api.get('/datasets/datasets/');
    return data.results || data;
  },

  async get(id: string): Promise<Dataset> {
    const { data } = await api.get(`/datasets/datasets/${id}/`);
    return data;
  },

  async upload(file: File, name?: string): Promise<Dataset> {
    const formData = new FormData();
    formData.append('file', file);
    if (name) formData.append('name', name);
    const { data } = await api.post('/datasets/datasets/upload/', formData, {
      headers: { 'Content-Type': 'multipart/form-data' },
    });
    return data;
  },

  async delete(id: string): Promise<void> {
    await api.delete(`/datasets/datasets/${id}/`);
  },

  async getPreview(id: string) {
    const { data } = await api.get(`/datasets/datasets/${id}/preview/`);
    return data;
  },
};
