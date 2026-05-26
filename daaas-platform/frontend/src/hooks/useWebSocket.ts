import { useEffect, useRef, useState } from 'react';

interface UseWebSocketOptions {
  url: string;
  onMessage?: (data: unknown) => void;
  autoConnect?: boolean;
}

export function useWebSocket({ url, onMessage, autoConnect = true }: UseWebSocketOptions) {
  const wsRef = useRef<WebSocket | null>(null);
  const [connected, setConnected] = useState(false);

  const connect = () => {
    const ws = new WebSocket(url);
    ws.onopen = () => setConnected(true);
    ws.onclose = () => setConnected(false);
    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      onMessage?.(data);
    };
    wsRef.current = ws;
  };

  const disconnect = () => {
    wsRef.current?.close();
    wsRef.current = null;
  };

  const send = (data: unknown) => {
    wsRef.current?.send(JSON.stringify(data));
  };

  useEffect(() => {
    if (autoConnect) connect();
    return () => disconnect();
  }, [url]);

  return { connected, send, connect, disconnect };
}
