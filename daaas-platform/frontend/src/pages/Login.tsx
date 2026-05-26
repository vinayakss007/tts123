import { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import Button from '@/components/common/Button';
import Input from '@/components/common/Input';
import { useAuthStore } from '@/store/authStore';

export default function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const { login, loading } = useAuthStore();
  const navigate = useNavigate();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await login(email, password);
      navigate('/');
    } catch {
      setError('Invalid email or password');
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50">
      <div className="w-full max-w-md p-8 bg-white rounded-xl shadow-sm">
        <h1 className="text-2xl font-bold text-center">DAaaS Platform</h1>
        <p className="text-center text-gray-500 mt-2">Sign in to your account</p>
        <form onSubmit={handleSubmit} className="mt-8 space-y-4">
          {error && <div className="text-sm text-red-600 text-center">{error}</div>}
          <Input label="Email" type="email" value={email} onChange={(e) => setEmail(e.target.value)} required />
          <Input label="Password" type="password" value={password} onChange={(e) => setPassword(e.target.value)} required />
          <Button type="submit" className="w-full" loading={loading}>Sign In</Button>
        </form>
        <p className="mt-4 text-sm text-center text-gray-500">
          No account? <Link to="/register" className="text-primary-600 hover:underline">Sign up</Link>
        </p>
      </div>
    </div>
  );
}
