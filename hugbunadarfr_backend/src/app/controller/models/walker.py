"""Walker class."""

from dataclasses import dataclass, field
from dataclasses_jsonschema import JsonSchemaMixin
from ..utils.attribute import Attribute
from uuid import UUID


@dataclass
class Walker(JsonSchemaMixin):
    """Walker entity."""

    is_available: bool = Attribute.new(
        "is_available",
        Attribute.required,
        Attribute.enforce_type
    )

    user_id: UUID = Attribute.new(
        "user_id",
        Attribute.required,
    )

    id: UUID = Attribute.new(
        "id",
        Attribute.enforce_type
    )
