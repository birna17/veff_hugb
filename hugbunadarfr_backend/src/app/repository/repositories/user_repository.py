"""User repository module."""

from .repository import Repository
from ..models.user import User
from ..data.data_provider import data
from ..exceptions.not_found_exception import NotFoundError


class UserRepository(Repository):
    """User repository."""

    def __init__(self, dog_owner_repository):
        """Initialize user repository."""
        model = User
        name = "Users"
        super().__init__(model=model, collection_name=name)
        self.__dog_owner_repository = dog_owner_repository

    def read_owners_of_dog(self, dog_id):
        """Get dogs associated with this user_id."""
        users = list()
        owners = self.__dog_owner_repository.search(f"dog_id=={dog_id}")
        for dog_owner in owners.to_list():
            try:
                user = self.read(dog_owner.owner_id)
                users.append(user)
            except NotFoundError:
                pass
        return users
