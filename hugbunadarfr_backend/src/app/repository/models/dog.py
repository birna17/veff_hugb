"""The dog class."""

from dataclasses import dataclass, field
from .entity import Entity
import json
from uuid import uuid4, UUID


@dataclass(eq=False)
class Dog(Entity):
    """A Dog entity, it contains a name, breed, and photo_url."""

    name: str = None
    breed: str = None
    photo_url: str = None
    override_id: UUID = None
    id: UUID = field(default_factory=uuid4, init=False)

    def set_name(self, new_name):
        """Set name of dog."""
        self.name = new_name

    def set_breed(self, new_breed):
        """Set breed of dog."""
        self.breed = new_breed

    def set_photo_url(self, new_photo_url):
        """Set photo_url of dog."""
        self.photo_url = new_photo_url

    def get_name(self):
        """Get name of dog."""
        return self.name

    def get_breed(self):
        """Get breed of dog."""
        return self.breed

    def get_photo_url(self):
        """Get photo_url of dog."""
        return self.photo_url
