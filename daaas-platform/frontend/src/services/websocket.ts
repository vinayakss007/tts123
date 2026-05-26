const WS_BASE = import.meta.env.VITE_WS_BASE_URL || 'ws://localhost:8000/ws';

export function createNotificationSocket(onMessage: (data: unknown) => void): WebSocket {
  const token = localStorage.getItem('access_token');
  const ws = new WebSocket(`${WS_BASE}/notifications/?token=${token}`);

  ws.onmessage = (event) => {
    const data = JSON.parse(event.data);
    onMessage(data);
  };

  return ws;
}
