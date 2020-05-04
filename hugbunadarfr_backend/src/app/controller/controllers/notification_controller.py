"""Controller for notification related functions."""
from ..models.user import User
from ..models.notification import Notification
from ..utils.request_utils import authenticated
from py_linq import Enumerable
from uuid import UUID, uuid4
from .controller import Controller


class NotificationController(Controller):
    """Retrieve notifications."""

    def __init__(self, repository_context: "RepositoryContext"):
        """Init a NotificationController, with a given repository_context."""
        super().__init__(repository_context)
        self.__repository_context = repository_context

    @authenticated
    async def get_notifications(self, request: "Request", unread=False):
        """Get notifications for user.

        :param unread: If true only returns unread notifications.
        """
        notifications = await self.__repository_context\
                                  .read_all_notifications()
        notifications = notifications\
            .where(lambda n: n.receiver_id == request.user_id)
        await self.mark_as_read(notifications)
        if unread:
            return notifications\
                .except_(lambda n: n.read is True)\
                .to_list()
        else:
            return notifications.to_list()

    async def mark_as_read(self, notifications):
        """Mark a list of notifications as read."""
        for notification in notifications:
            if not notification.read:
                notification.read = True
                await self.__repository_context\
                    .update_notification(notification, notification.id)

    async def _notify_walk_request(self, receiver_id: UUID, sender_id: UUID):
        """Send a walk request notification to a dog walker.

        :param receiver: The receiver of the notification.
        :param sender: The 'sender' of the notification.

        Should not be used as a command through websocket.
        """
        await self._notify(
            "You got a new order request!", receiver_id, sender_id
        )

    async def _notify_walk_request_rejected(
        self, receiver_id: UUID, sender_id: UUID
    ):
        """Notify a user that a walk request was rejected.

        Should not be used as a command through websocket.
        """
        await self._notify(
            "Your walk request was rejected. Sorry about that :(",
            receiver_id, sender_id
        )

    async def _notify_walk_request_accepted(
        self, receiver_id: UUID, sender_id: UUID
    ):
        """Notify a user that a walk request was accepted.

        Should not be used as a command through websocket.
        """
        await self._notify(
            "Your walk request was accepted. The walker is on their way :)",
            receiver_id, sender_id
        )

    async def _notify(self, message: str, receiver_id: UUID, sender_id: UUID):
        """Send a notification.

        :param message: The message that will be sent.
        :param receiver: The receiver of the notification.
        :param sender: The 'sender' of the notification.

        Should not be used as a command through websocket.
        """
        await self.__repository_context.create_notification(
            Notification(
                message=message,
                receiver_id=receiver_id,
                sender_id=sender_id,
                read=False
            )
        )

    @property
    def actions(self) -> dict:
        """Read-only property that returns a dict of all functions.

        The key is the function name to expose, and the value is the
        function itself.
        """
        return {
            "get_notifications": self.get_notifications
        }
