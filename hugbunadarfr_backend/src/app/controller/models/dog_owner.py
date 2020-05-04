"""DogOwner module."""

from dataclasses import dataclass, field
from uuid import UUID
import json
from dataclasses_jsonschema import JsonSchemaMixin
from ..utils.attribute import Attribute


@dataclass
class DogOwner(JsonSchemaMixin):
    """Dog owner model."""

    owner_id: UUID = Attribute.new(
        "owner_id",
        Attribute.required,
        Attribute.enforce_type
    )
    dog_id: UUID = Attribute.new(
        "dog_id",
        Attribute.required,
        Attribute.enforce_type
    )
    id: UUID = Attribute.new(
        "id",
        Attribute.enforce_type
    )
