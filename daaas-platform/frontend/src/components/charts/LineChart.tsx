import Plot from 'react-plotly.js';
import ChartContainer from './ChartContainer';

interface LineChartProps {
  title?: string;
  data: { x: number[]; y: number[]; name?: string }[];
  xTitle?: string;
  yTitle?: string;
}

export default function LineChart({ title, data, xTitle, yTitle }: LineChartProps) {
  const traces = data.map((series) => ({
    x: series.x,
    y: series.y,
    type: 'scatter' as const,
    mode: 'lines' as const,
    name: series.name || '',
  }));

  return (
    <ChartContainer title={title}>
      <Plot
        data={traces}
        layout={{
          autosize: true,
          margin: { t: 20, r: 20, b: 40, l: 50 },
          xaxis: { title: xTitle },
          yaxis: { title: yTitle },
          showlegend: data.length > 1,
        }}
        config={{ responsive: true, displayModeBar: false }}
        style={{ width: '100%', height: '100%' }}
      />
    </ChartContainer>
  );
}
