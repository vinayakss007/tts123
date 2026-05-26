import { useState } from 'react';
import { analyticsService } from '@/services/analytics';

export function useAnalytics() {
  const [loading, setLoading] = useState(false);

  const runAnalysis = async (sessionId: string) => {
    setLoading(true);
    try {
      await analyticsService.runSession(sessionId);
    } finally {
      setLoading(false);
    }
  };

  return { runAnalysis, loading };
}
