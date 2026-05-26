"""WebSocket consumers for real-time notifications."""
import json

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer


class NotificationConsumer(AsyncWebsocketConsumer):
    """WebSocket consumer for real-time notification delivery.

    Clients connect to receive push notifications about:
    - Dataset processing completion
    - ML training progress
    - Report generation status
    - System alerts
    """

    async def connect(self):
        """Accept WebSocket connection and add to user group."""
        self.user = self.scope["user"]

        if self.user.is_anonymous:
            await self.close()
            return

        self.group_name = f"notifications_{self.user.id}"
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

        # Send unread count on connect
        unread_count = await self._get_unread_count()
        await self.send(json.dumps({
            "type": "connection_established",
            "unread_count": unread_count,
        }))

    async def disconnect(self, close_code):
        """Remove from notification group on disconnect."""
        if hasattr(self, "group_name"):
            await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        """Handle incoming WebSocket messages (e.g., mark as read)."""
        data = json.loads(text_data)
        action = data.get("action")

        if action == "mark_read":
            notification_id = data.get("notification_id")
            await self._mark_as_read(notification_id)
        elif action == "mark_all_read":
            await self._mark_all_as_read()

    async def notification_message(self, event):
        """Send notification to WebSocket client."""
        await self.send(json.dumps({
            "type": "notification",
            "data": event["data"],
        }))

    @database_sync_to_async
    def _get_unread_count(self) -> int:
        """Get count of unread notifications for user."""
        from .models import Notification

        return Notification.objects.filter(user=self.user, is_read=False).count()

    @database_sync_to_async
    def _mark_as_read(self, notification_id: str):
        """Mark a specific notification as read."""
        from .models import Notification

        Notification.objects.filter(id=notification_id, user=self.user).update(is_read=True)

    @database_sync_to_async
    def _mark_all_as_read(self):
        """Mark all notifications as read for user."""
        from .models import Notification

        Notification.objects.filter(user=self.user, is_read=False).update(is_read=True)
