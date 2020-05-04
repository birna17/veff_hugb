"""The notification model keeps track of users in the system."""

from dataclasses import dataclass, field
from uuid import UUID, uuid4
from .entity import Entity


@dataclass(eq=False)
class Notification(Entity):
    """The notification entity."""

    message: str = None
    sender_id: UUID = None
    receiver_id: UUID = None
    override_id: UUID = None
    read: bool = False
    id: UUID = field(default_factory=uuid4, init=False)
