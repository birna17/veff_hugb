"""User class."""

from dataclasses import dataclass, field
from dataclasses_jsonschema import JsonSchemaMixin
from uuid import UUID
from ..utils.attribute import Attribute


@dataclass
class User(JsonSchemaMixin):
    """User entity."""

    username: str = Attribute.new(
        "username",
        Attribute.required,
        Attribute.enforce_type,
        Attribute.min_length(1)
    )

    password: str = Attribute.new(
        "password",
        Attribute.required,
        Attribute.enforce_type,
        Attribute.min_length(4)
    )

    first_name: str = Attribute.new(
        "first_name",
        Attribute.required,
        Attribute.enforce_type
    )

    last_name: str = Attribute.new(
        "last_name",
        Attribute.required,
        Attribute.enforce_type
    )

    address: str = Attribute.new(
        "address",
        Attribute.required,
        Attribute.enforce_type
    )

    phone_number: str = Attribute.new(
        "phone_number",
        Attribute.required,
        Attribute.enforce_type,
        Attribute.phone_number
    )

    email_address: str = Attribute.new(
        "email_address",
        Attribute.required,
        Attribute.enforce_type,
        Attribute.email
    )

    id: UUID = Attribute.new(
        "id",
        Attribute.enforce_type
    )
