import { CHART_COLORS } from './constants';

export function getChartColor(index: number): string {
  return CHART_COLORS[index % CHART_COLORS.length];
}

export function generateChartLayout(title?: string, xTitle?: string, yTitle?: string) {
  return {
    autosize: true,
    title: title || undefined,
    margin: { t: title ? 40 : 20, r: 20, b: 40, l: 50 },
    xaxis: { title: xTitle },
    yaxis: { title: yTitle },
    font: { family: 'Inter, system-ui, sans-serif', size: 12 },
    plot_bgcolor: 'transparent',
    paper_bgcolor: 'transparent',
  };
}

export function formatAxisLabel(value: number): string {
  if (Math.abs(value) >= 1_000_000) return `${(value / 1_000_000).toFixed(1)}M`;
  if (Math.abs(value) >= 1_000) return `${(value / 1_000).toFixed(1)}K`;
  return value.toString();
}
