"""DogOwner module."""

from dataclasses import dataclass, field
from uuid import UUID, uuid4
from .entity import Entity


@dataclass(eq=False)
class DogOwner(Entity):
    """DogOwner model."""

    owner_id: UUID = None
    dog_id: UUID = None
    override_id: UUID = None
    id: UUID = field(default_factory=uuid4, init=False)

    def get_owner_id(self):
        """Get the owner id."""
        return self.owner_id

    def get_dog_id(self):
        """Get the dog id."""
        return self.dog_id
