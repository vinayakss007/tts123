import { Database, BarChart3, Brain, FileText } from 'lucide-react';

export default function Dashboard() {
  const stats = [
    { label: 'Datasets', value: '12', icon: Database, color: 'bg-blue-100 text-blue-600' },
    { label: 'Analyses', value: '8', icon: BarChart3, color: 'bg-green-100 text-green-600' },
    { label: 'ML Models', value: '3', icon: Brain, color: 'bg-purple-100 text-purple-600' },
    { label: 'Reports', value: '5', icon: FileText, color: 'bg-orange-100 text-orange-600' },
  ];

  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold">Dashboard</h1>
      <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-4">
        {stats.map((stat) => (
          <div key={stat.label} className="card flex items-center gap-4">
            <div className={`p-3 rounded-lg ${stat.color}`}>
              <stat.icon size={24} />
            </div>
            <div>
              <p className="text-sm text-gray-500">{stat.label}</p>
              <p className="text-2xl font-bold">{stat.value}</p>
            </div>
          </div>
        ))}
      </div>
      <div className="card">
        <h2 className="text-lg font-medium mb-4">Recent Activity</h2>
        <p className="text-gray-500 text-sm">No recent activity to show.</p>
      </div>
    </div>
  );
}
