"""Walker repository module."""

from .walkrequest_repository import WalkRequestRepository
from .user_repository import UserRepository
from random import randint

from random import randint
from dataclasses import asdict
from ..models.user import User
from ..models.walker import Walker
from ..data.data_provider import data
from ..exceptions.not_enough_walkers_exception import NotEnoughWalkersException
from .repository import Repository


class WalkerRepository(Repository):
    """Walker repository class."""

    def __init__(self, walk_request_repository, user_repository):
        """Initialize walker repository."""
        model = Walker
        name = "Walkers"
        super().__init__(model=model, collection_name=name)
        self.walk_request_repository = walk_request_repository
        self.user_repository = user_repository

    def get_random_walkers(self, count):
        """Get n random available walkers, where n=count."""
        available_walkers = [w for w in self.read_all()
                             if w.get_availability()]

        if len(available_walkers) < count:
            raise NotEnoughWalkersException
        elif len(available_walkers) == count:
            return available_walkers

        random_walkers = list()
        for i in count:
            random_walkers.append(available_walkers[
                randint(0, len(available_walkers) - 1)])

        return random_walkers

    def set_as_walker(self, user_id):
        """Set user as walker."""
        user = self.user_repository.read(user_id)
        user_dict = asdict(user)
        user_dict["override_id"] = user_dict["id"]
        del user_dict["id"]
        user_dict["is_available"] = False
        self.create(user_dict)

    def request_walker(self, owner_id, dog_id, walker_id, time_start,
                       time_end):
        """Put a request in for a specified walker."""
        return self.walk_request_repository.create({
            "owner_id": owner_id,
            "walker_id": walker_id,
            "dog_id": dog_id,
            "status": "Pending",
            "time_start": time_start,
            "time_end": time_end
        })

    def get_requests(self, walker_id):
        """Get all requests for specified walker."""
        requests = list()

        for request in self.walk_request_repository.read_all():
            if str(request.walker_id) == str(walker_id):
                requests.append(self.read(str(request.walker_id)))
        return requests
