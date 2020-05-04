"""Walker module containing walker dataclass."""

from dataclasses import dataclass, field
from .entity import Entity
from uuid import UUID, uuid4


@dataclass(eq=False)
class Walker(Entity):
    """Walker Model."""

    is_available: bool = None
    user_id: UUID = None
    override_id: UUID = None
    id: UUID = field(default_factory=uuid4, init=False)

    def set_availability(self, availability):
        """Avalabulity of walker."""
        self.is_available = availability

    def get_availability(self):
        """Get the avalability."""
        return self.is_available
