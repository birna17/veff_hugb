"""Walk requests are relational entities."""
from datetime import datetime
from dataclasses import dataclass, field
from .entity import Entity
from uuid import UUID, uuid4


@dataclass(eq=False)
class WalkRequest(Entity):
    """WalkRequest entity.

    Connects owners, dogs and walkers.
    """

    owner_id: UUID = None
    walker_id: UUID = None
    dog_id: UUID = None
    status: str = None
    time_start: datetime = None
    time_end: datetime = None
    override_id: UUID = None
    id: UUID = field(default_factory=uuid4, init=False)
