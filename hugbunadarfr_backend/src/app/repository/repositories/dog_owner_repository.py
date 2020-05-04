"""Dog repository module."""
from os.path import defpath

from ..models.dog_owner import DogOwner
from ..data.data_provider import data
from .repository import Repository


class DogOwnerRepository(Repository):
    """Dog owner repository class."""

    def __init__(self):
        """Initialize dog owner repository."""
        model = DogOwner
        name = "DogOwners"
        super().__init__(model=model, collection_name=name)
