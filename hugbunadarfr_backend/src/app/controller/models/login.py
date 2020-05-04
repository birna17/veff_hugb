"""Login class."""

from dataclasses import dataclass, field
from dataclasses_jsonschema import JsonSchemaMixin
from ..utils.attribute import Attribute
from datetime import datetime, timedelta
from uuid import UUID, uuid4


@dataclass
class Login(JsonSchemaMixin):
    """Login entity."""

    user_id: UUID = Attribute.new(
        "user_id",
        Attribute.required,
        Attribute.enforce_type
    )

    log_token: UUID = Attribute.new(
        "log_token",
        Attribute.enforce_type,
    )

    log_date: datetime = Attribute.new(
        "log_date",
        Attribute.required,
        Attribute.enforce_type,
    )

    log_expiry_date: datetime = Attribute.new(
        "log_expiry_date",
        Attribute.enforce_type,
        Attribute.required,
    )

    id: UUID = Attribute.new(
        "id",
        Attribute.enforce_type
    )
