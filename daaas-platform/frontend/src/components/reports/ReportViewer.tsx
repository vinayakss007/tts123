interface ReportViewerProps {
  title: string;
  sections: { title: string; content: string; type: string }[];
  status: string;
}

export default function ReportViewer({ title, sections, status }: ReportViewerProps) {
  if (status === 'generating') {
    return (
      <div className="card text-center py-12">
        <div className="animate-spin h-8 w-8 border-4 border-primary-600 border-t-transparent rounded-full mx-auto" />
        <p className="mt-4 text-gray-600">Generating report...</p>
      </div>
    );
  }

  return (
    <div className="card">
      <h2 className="text-xl font-bold mb-6">{title}</h2>
      <div className="space-y-6">
        {sections.map((section, idx) => (
          <div key={idx}>
            <h3 className="text-lg font-medium text-gray-800 mb-2">{section.title}</h3>
            <div className="prose prose-sm max-w-none text-gray-600">{section.content}</div>
          </div>
        ))}
      </div>
    </div>
  );
}
