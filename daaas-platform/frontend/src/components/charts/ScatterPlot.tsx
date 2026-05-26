import Plot from 'react-plotly.js';
import ChartContainer from './ChartContainer';

interface ScatterPlotProps {
  title?: string;
  x: number[];
  y: number[];
  xTitle?: string;
  yTitle?: string;
  color?: string;
}

export default function ScatterPlot({ title, x, y, xTitle, yTitle, color }: ScatterPlotProps) {
  return (
    <ChartContainer title={title}>
      <Plot
        data={[{ x, y, type: 'scatter' as const, mode: 'markers' as const, marker: { color, size: 8 } }]}
        layout={{
          autosize: true,
          margin: { t: 20, r: 20, b: 40, l: 50 },
          xaxis: { title: xTitle },
          yaxis: { title: yTitle },
        }}
        config={{ responsive: true, displayModeBar: false }}
        style={{ width: '100%', height: '100%' }}
      />
    </ChartContainer>
  );
}
