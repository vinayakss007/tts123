import api from './api';

export const authService = {
  async login(email: string, password: string) {
    const { data } = await api.post('/accounts/token/', { email, password });
    return data;
  },

  async register(email: string, password: string, firstName: string, lastName: string) {
    const { data } = await api.post('/accounts/register/', {
      email,
      password,
      password_confirm: password,
      first_name: firstName,
      last_name: lastName,
    });
    return data;
  },

  async getProfile() {
    const { data } = await api.get('/accounts/users/me/');
    return data;
  },

  async updateProfile(updates: Record<string, string>) {
    const { data } = await api.patch('/accounts/users/me/', updates);
    return data;
  },
};
