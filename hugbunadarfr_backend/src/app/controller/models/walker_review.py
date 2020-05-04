"""WalkerReview class."""

from dataclasses import dataclass, field
from dataclasses_jsonschema import JsonSchemaMixin
from ..utils.attribute import Attribute
from uuid import UUID


@dataclass
class WalkerReview(JsonSchemaMixin):
    """WalkerReview entity."""

    walker_id: UUID = Attribute.new(
        "walker_id",
        Attribute.required,
        Attribute.enforce_type
    )

    rating: int = Attribute.new(
        "rating",
        Attribute.required,
        Attribute.enforce_type,
        Attribute.max_length(1)
    )

    id: UUID = Attribute.new(
        "id",
        Attribute.enforce_type
    )
