"""Entity model base."""

from dataclasses import dataclass, fields, is_dataclass
from abc import ABC, abstractmethod
from uuid import uuid4, UUID
import json


@dataclass(eq=False)
class Entity(ABC):
    """Entity model base class."""

    def __init__(self, *args, **kwargs):
        """Init an entity."""
        self.id: UUID = uuid4()
        self.override_id: UUID = kwargs.get("override_id", None)
        super().__init__()
        self.__post_init__()

    def __post_init__(self):
        """Handle overriding the ID."""
        if self.override_id is not None:
            self.id = UUID(str(self.override_id))
        try:
            del self.__dataclass_fields__["override_id"]
        except (KeyError, AttributeError):
            pass

    def __eq__(self, other: "Entity"):
        """Equality is based on the objects ID."""
        if isinstance(other, type(self)):
            return str(self.id) == str(other.id)
        return str(self.id) == other

    def get_id(self) -> UUID:
        """Get the objects unique UUID."""
        return self.id
