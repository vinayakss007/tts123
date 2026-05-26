import { ReactNode } from 'react';

interface ChartContainerProps {
  title?: string;
  children: ReactNode;
  className?: string;
}

export default function ChartContainer({ title, children, className = '' }: ChartContainerProps) {
  return (
    <div className={`bg-white rounded-xl border border-gray-200 p-4 ${className}`}>
      {title && <h3 className="text-sm font-medium text-gray-700 mb-3">{title}</h3>}
      <div className="w-full h-64">{children}</div>
    </div>
  );
}
