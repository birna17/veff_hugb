"""WalkRequest class."""

from dataclasses import dataclass, field
from datetime import datetime
from dataclasses_jsonschema import JsonSchemaMixin
from ..utils.attribute import Attribute
from uuid import UUID


@dataclass
class WalkRequest(JsonSchemaMixin):
    """WalkRequest entity."""

    owner_id: UUID = Attribute.new(
        "owner_id",
        Attribute.required,
        Attribute.enforce_type
    )

    walker_id: UUID = Attribute.new(
        "walker_id",
        Attribute.required,
        Attribute.enforce_type
    )

    dog_id: UUID = Attribute.new(
        "dog_id",
        Attribute.required,
        Attribute.enforce_type
    )

    status: str = Attribute.new(
        "status",
        Attribute.enforce_type,
        default="PENDING"
    )

    time_start: datetime = Attribute.new(
        "time_start",
        Attribute.enforce_type
    )

    time_end: datetime = Attribute.new(
        "time_end",
        Attribute.enforce_type
    )

    id: UUID = Attribute.new(
        "id",
        Attribute.enforce_type
    )
