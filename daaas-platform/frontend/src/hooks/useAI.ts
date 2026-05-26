import { useState } from 'react';
import { aiGatewayService } from '@/services/aiGateway';

export function useAI() {
  const [loading, setLoading] = useState(false);
  const [response, setResponse] = useState<string | null>(null);

  const complete = async (messages: { role: string; content: string }[]) => {
    setLoading(true);
    try {
      const result = await aiGatewayService.completion(messages);
      setResponse(result.content);
      return result;
    } finally {
      setLoading(false);
    }
  };

  return { complete, loading, response };
}
