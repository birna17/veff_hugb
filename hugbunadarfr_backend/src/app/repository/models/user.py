"""The user model keeps track of users in the system."""

from dataclasses import dataclass, field
from uuid import UUID, uuid4
from .entity import Entity


@dataclass(eq=False)
class User(Entity):
    """The user entity."""

    username: str = None
    password: str = None
    first_name: str = None
    last_name: str = None
    address: str = None
    phone_number: str = None
    email_address: str = None
    override_id: UUID = None
    id: UUID = field(default_factory=uuid4, init=False)

    # methods

    def get_username(self):
        """Get Users username."""
        return self.username

    def get_password(self):
        """Get Users password."""
        return self.password

    def get_full_name(self):
        """Get Users full name."""
        return self.first_name + " " + self.last_name

    def get_first_name(self):
        """Get User first name."""
        return self.first_name

    def get_last_name(self):
        """Get User last name."""
        return self.last_name

    def get_address(self):
        """Get Users address."""
        return self.address

    def get_phone_number(self):
        """Get Users phone number."""
        return self.phone_number

    def get_email_address(self):
        """Get Users email address."""
        return self.email_address
