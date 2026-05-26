import ReportBuilder from '@/components/reports/ReportBuilder';

export default function Reports() {
  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold">AI-Powered Reports</h1>
      <div className="grid gap-6 lg:grid-cols-3">
        <div className="lg:col-span-2">
          <div className="card">
            <p className="text-gray-500">Generated reports will appear here.</p>
          </div>
        </div>
        <div>
          <ReportBuilder datasets={[]} onGenerate={() => {}} />
        </div>
      </div>
    </div>
  );
}
