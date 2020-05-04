"""The dog class."""

from dataclasses import dataclass, field
from dataclasses_jsonschema import JsonSchemaMixin
from ..utils.attribute import Attribute
from uuid import UUID
import json


# @dataclass_json
@dataclass
class Dog(JsonSchemaMixin):
    """A Dog entity, it contains a name, breed, and photo_url."""

    name: str = Attribute.new(
        "name",
        Attribute.required,
        Attribute.enforce_type,
        Attribute.min_length(3),
    )
    breed: str = Attribute.new(
        "breed",
        Attribute.required,
        Attribute.enforce_type,
        Attribute.min_length(3),
    )
    photo_url: str = Attribute.new(
        "photo_url",
        Attribute.required,
        Attribute.url,
    )
    id: UUID = Attribute.new(
        "id",
        Attribute.enforce_type
    )
