"""Notification repository module."""
from .repository import Repository
from ..models.notification import Notification


class NotificationRepository(Repository):
    """Notification repository."""

    def __init__(self):
        """Initialize notification repository."""
        model = Notification
        name = "Notifications"
        super().__init__(model=model, collection_name=name)
