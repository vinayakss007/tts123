import Plot from 'react-plotly.js';
import ChartContainer from './ChartContainer';

interface BarChartProps {
  title?: string;
  categories: string[];
  values: number[];
  orientation?: 'v' | 'h';
  color?: string;
}

export default function BarChart({ title, categories, values, orientation = 'v', color }: BarChartProps) {
  const trace = orientation === 'v'
    ? { x: categories, y: values, type: 'bar' as const, marker: { color } }
    : { y: categories, x: values, type: 'bar' as const, orientation: 'h' as const, marker: { color } };

  return (
    <ChartContainer title={title}>
      <Plot
        data={[trace]}
        layout={{
          autosize: true,
          margin: { t: 20, r: 20, b: 40, l: 80 },
          showlegend: false,
        }}
        config={{ responsive: true, displayModeBar: false }}
        style={{ width: '100%', height: '100%' }}
      />
    </ChartContainer>
  );
}
