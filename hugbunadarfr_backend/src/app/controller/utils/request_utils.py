"""Request utilities."""
from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID
from ..exceptions.authentication_error import AuthenticationError


@dataclass
class Request():
    """Request object for controllers."""

    access_token: str = None
    authenticated: bool = False
    date: datetime = field(default_factory=datetime.now)
    user_id: UUID = None
    walker_id: UUID = None
    login: "Login" = None


def authenticated(func):
    """Decorator, check if a request has been authenticated."""
    def wrapper(self, request: Request, *args, **kwargs):
        if not isinstance(request, Request):
            raise TypeError("Request is not a valid parameter")
        if request.authenticated:
            if request.login.log_expiry_date < datetime.now():
                raise AuthenticationError("access_token expired")
            return func(self, request, *args, **kwargs)
        else:
            raise AuthenticationError("User is not authenticated.")
    return wrapper


def is_walker(func):
    """Decorator, check if a request user is a walker."""
    async def wrapper(self, request, *args, **kwargs):
        walkers = await self.get_repository_context().search_walkers(
            f"user_id=={request.user_id}"
        )
        if walkers.first_or_default() is None:
            raise AuthenticationError("User is not a walker.")
        request.walker_id = walkers.first_or_default().id
        return await func(self, request, *args, **kwargs)
    return wrapper
