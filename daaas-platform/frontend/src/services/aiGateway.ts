import api from './api';

interface AIMessage {
  role: string;
  content: string;
}

interface AICompletionResponse {
  content: string;
  provider: string;
  model: string;
  usage: { prompt_tokens: number; completion_tokens: number; total_tokens: number };
  latency_ms: number;
}

export const aiGatewayService = {
  async completion(messages: AIMessage[], options?: { provider?: string; maxTokens?: number }): Promise<AICompletionResponse> {
    const { data } = await api.post('/ai/completions/', {
      messages,
      provider: options?.provider,
      max_tokens: options?.maxTokens || 4096,
    });
    return data;
  },

  streamCompletion(messages: AIMessage[], onChunk: (chunk: string) => void): EventSource {
    // Use EventSource for SSE streaming
    const eventSource = new EventSource(`${api.defaults.baseURL}/ai/stream/`);
    eventSource.onmessage = (event) => {
      const data = JSON.parse(event.data);
      if (data.type === 'content') onChunk(data.content);
    };
    return eventSource;
  },
};
