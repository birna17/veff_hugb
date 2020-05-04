"""The login model kepps track of the users that are.

loged in at a given moment.
"""

import datetime
from dataclasses import dataclass, field
from uuid import UUID, uuid4
from .entity import Entity


@dataclass(eq=False)
class Login(Entity):
    """The login entity contains user id, login token."""

    """id and the time of login."""

    user_id: UUID = None
    log_token: UUID = field(default_factory=uuid4)
    log_date: datetime.datetime = None
    log_expiry_date: datetime.datetime = None
    override_id: UUID = None
    id: UUID = field(default_factory=uuid4, init=False)

    # Metods

    def get_user_id(self):
        """Get user id."""
        return self.user_id

    def get_token(self):
        """Get token."""
        return self.log_token

    def get_date(self):
        """Get date of log."""
        return self.log_date
