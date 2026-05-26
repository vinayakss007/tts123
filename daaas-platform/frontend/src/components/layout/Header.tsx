import { Bell, Search, User } from 'lucide-react';
import { useAuthStore } from '@/store/authStore';

export default function Header() {
  const { user } = useAuthStore();

  return (
    <header className="bg-white border-b border-gray-200 px-6 py-4">
      <div className="flex items-center justify-between">
        <div className="flex items-center flex-1">
          <div className="relative w-96">
            <Search className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400" size={18} />
            <input
              type="text"
              placeholder="Search datasets, analyses, reports..."
              className="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-primary-500"
            />
          </div>
        </div>
        <div className="flex items-center gap-4">
          <button className="relative text-gray-500 hover:text-gray-700">
            <Bell size={20} />
            <span className="absolute -top-1 -right-1 h-4 w-4 bg-red-500 rounded-full text-xs text-white flex items-center justify-center">
              3
            </span>
          </button>
          <div className="flex items-center gap-2">
            <div className="h-8 w-8 bg-primary-100 rounded-full flex items-center justify-center">
              <User size={16} className="text-primary-600" />
            </div>
            <span className="text-sm font-medium">{user?.first_name || 'User'}</span>
          </div>
        </div>
      </div>
    </header>
  );
}
