"""WalkerReview."""

from dataclasses import dataclass, field
from uuid import UUID, uuid4
from .entity import Entity


@dataclass(eq=False)
class WalkerReview(Entity):
    """WalkerReview model class."""

    walker_id: UUID = None
    rating: int = None
    override_id: UUID = None
    id: UUID = field(default_factory=uuid4, init=False)
