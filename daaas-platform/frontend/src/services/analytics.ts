import api from './api';

export const analyticsService = {
  async listSessions() {
    const { data } = await api.get('/analytics/sessions/');
    return data.results || data;
  },

  async createSession(payload: { name: string; dataset: string }) {
    const { data } = await api.post('/analytics/sessions/', payload);
    return data;
  },

  async runSession(sessionId: string) {
    const { data } = await api.post(`/analytics/sessions/${sessionId}/run/`);
    return data;
  },

  async addStep(sessionId: string, step: { step_type: string; parameters: Record<string, unknown> }) {
    const { data } = await api.post(`/analytics/sessions/${sessionId}/add_step/`, step);
    return data;
  },
};
