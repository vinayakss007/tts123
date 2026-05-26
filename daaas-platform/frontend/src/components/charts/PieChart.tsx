import Plot from 'react-plotly.js';
import ChartContainer from './ChartContainer';

interface PieChartProps {
  title?: string;
  labels: string[];
  values: number[];
}

export default function PieChart({ title, labels, values }: PieChartProps) {
  return (
    <ChartContainer title={title}>
      <Plot
        data={[{ labels, values, type: 'pie' as const, hole: 0.4 }]}
        layout={{
          autosize: true,
          margin: { t: 20, r: 20, b: 20, l: 20 },
          showlegend: true,
        }}
        config={{ responsive: true, displayModeBar: false }}
        style={{ width: '100%', height: '100%' }}
      />
    </ChartContainer>
  );
}
