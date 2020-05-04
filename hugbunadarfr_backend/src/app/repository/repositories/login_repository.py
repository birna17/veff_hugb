"""login repository module."""
from os.path import defpath

from .repository import Repository
from ..models.login import Login
from ..data.data_provider import data
from .user_repository import UserRepository


class LoginRepository(Repository):
    """Login repository."""

    def __init__(self, user_repository):
        """Initialize user repository."""
        model = Login
        name = "Logins"
        self.user_repository = user_repository
        super().__init__(model=model, collection_name=name)
