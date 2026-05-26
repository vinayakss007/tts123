import { NavLink } from 'react-router-dom';
import {
  LayoutDashboard,
  Database,
  BarChart3,
  Brain,
  FileText,
  CreditCard,
  Settings,
  LogOut,
} from 'lucide-react';
import { useAuthStore } from '@/store/authStore';

const navigation = [
  { name: 'Dashboard', to: '/', icon: LayoutDashboard },
  { name: 'Datasets', to: '/datasets', icon: Database },
  { name: 'Analytics', to: '/analytics', icon: BarChart3 },
  { name: 'ML Models', to: '/ml-models', icon: Brain },
  { name: 'Reports', to: '/reports', icon: FileText },
  { name: 'Billing', to: '/billing', icon: CreditCard },
  { name: 'Settings', to: '/settings', icon: Settings },
];

export default function Sidebar() {
  const { logout } = useAuthStore();

  return (
    <aside className="w-64 bg-gray-900 text-white flex flex-col h-screen">
      <div className="p-6">
        <h1 className="text-xl font-bold">DAaaS</h1>
        <p className="text-xs text-gray-400 mt-1">Data Analytics as a Service</p>
      </div>
      <nav className="flex-1 px-4 space-y-1">
        {navigation.map((item) => (
          <NavLink
            key={item.name}
            to={item.to}
            end={item.to === '/'}
            className={({ isActive }) =>
              `flex items-center gap-3 px-3 py-2 rounded-lg text-sm transition-colors ${
                isActive
                  ? 'bg-primary-600 text-white'
                  : 'text-gray-300 hover:bg-gray-800 hover:text-white'
              }`
            }
          >
            <item.icon size={18} />
            {item.name}
          </NavLink>
        ))}
      </nav>
      <div className="p-4 border-t border-gray-800">
        <button
          onClick={logout}
          className="flex items-center gap-3 px-3 py-2 text-sm text-gray-300 hover:text-white w-full rounded-lg hover:bg-gray-800"
        >
          <LogOut size={18} />
          Sign Out
        </button>
      </div>
    </aside>
  );
}
