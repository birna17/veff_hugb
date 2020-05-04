"""Notification model module."""
from dataclasses_jsonschema import JsonSchemaMixin
from dataclasses import dataclass, field
from ..utils.attribute import Attribute
from .user import User
from uuid import UUID


@dataclass
class Notification(JsonSchemaMixin):
    """Notification entity."""

    message: str = Attribute.new(
        "message",
        Attribute.required,
        Attribute.enforce_type
    )

    read: bool = Attribute.new(
        "read",
        Attribute.required,
        Attribute.enforce_type
    )

    sender_id: UUID = Attribute.new(
        "sender_id",
        Attribute.required,
        Attribute.enforce_type
    )

    receiver_id: UUID = Attribute.new(
        "receiver_id",
        Attribute.required,
        Attribute.enforce_type
    )

    id: UUID = Attribute.new(
        "id",
        Attribute.enforce_type
    )
