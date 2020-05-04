"""Dog repository module."""
from os.path import defpath

from ..models.dog import Dog
from ..data.data_provider import data
from .repository import Repository
from ..exceptions.not_found_exception import NotFoundError


class DogRepository(Repository):
    """Dog repository class."""

    def __init__(self, dog_owner_repository):
        """Initialize dog repository."""
        model = Dog
        name = "Dogs"
        super().__init__(model=model, collection_name=name)
        self.__dog_owner_repository = dog_owner_repository

    def read_dogs_of_owner(self, owner_id):
        """Get dogs associated with this user_id."""
        dogs = list()
        owners = self.__dog_owner_repository.search(f"owner_id=={owner_id}")
        for dog_owner in owners.to_list():
            try:
                dog = self.read(dog_owner.dog_id)
                dogs.append(dog)
            except NotFoundError:
                pass
        return dogs
