"""The Controller for any actions related to walks."""
from random import choices
import asyncio
from datetime import datetime
from ..utils.request_utils import authenticated, is_walker
from ..models import WalkRequest
from .controller import Controller


class WalkController(Controller):
    """Manage and retrieve data related to dog walks."""

    def __init__(self, repository_context: "RepositoryContext",
                 notification_controller: "NotificationController"):
        """Init a new WalkController, with a given repository_context."""
        super().__init__(repository_context)
        self.__repository_context = repository_context
        self.__notification_controller = notification_controller

    @property
    def actions(self) -> dict:
        """Read-only property that returns a dict of all functions.

        The key is the function name to expose, and the value is the
        function itself.
        """
        return {
            "get_top_5_walkers": self.get_top_5_walkers,
            "get_new_top_5_walkers": self.get_new_top_5_walkers,
            "order_walker": self.order_walker,
            "my_ordered_walks": self.my_ordered_walks,
            "accept_walk": self.accept_walk,
            "complete_walk": self.complete_walk,
            "set_availability": self.set_availability,
            "my_walks": self.my_walks
        }

    async def get_top_5_walkers(self, request) -> list:
        """Return a list of 5 walkers, they need to be chosen based on some.

        criteria, but we can start off by just choosing 5 random
        walkers.
        """
        walkers = await self.__repository_context.read_all_walkers()
        walkers = walkers.where(lambda x: x.is_available)
        return choices(list(walkers), k=5)

    async def get_new_top_5_walkers(self, request) -> list:
        """Return a list 5 random walkers again."""
        return await self.get_top_5_walkers(request)

    @authenticated
    async def order_walker(self, request, walker_id, dog_id):
        """Order a walker to walk the given dog.

        The owners ID should be accessable in the request object
        """
        walker = await self.__repository_context.read_walker(walker_id)
        dog = await self.__repository_context.read_dog(dog_id)
        my_dogs = await self.__repository_context.read_dogs_of_owner(
            request.user_id
        )
        if dog not in my_dogs:
            raise Exception("Not your dog!")

        walk_request = await self.__repository_context.create_walkrequest(
            WalkRequest(
                owner_id=request.user_id,
                walker_id=walker_id,
                dog_id=dog_id,
                time_start=datetime.now()
            )
        )

        await self.__notification_controller\
            ._notify_walk_request(walker_id, request.user_id)
        return walk_request

    @authenticated
    async def my_ordered_walks(self, request):
        """Get a list of walks a user has ordered."""
        return await self.__repository_context.search(
            "WalkRequest", f"owner_id=={request.user_id}"
        )

    @is_walker
    @authenticated
    async def my_walks(self, request):
        """Get a list of walks a walker has participated in."""
        return await self.__repository_context.search(
            "WalkRequest", f"walker_id=={request.user_id}"
        )

    @is_walker
    @authenticated
    async def accept_walk(self, request, walk_request_id: "UUID"):
        """Accept a walk request as a walker."""
        walk_request = await self.__repository_context.read_walkrequest(
            walk_request_id
        )
        if walk_request.status != "PENDING":
            raise ValueError("Can't accept a non-pending walk request")
        if walk_request.walker_id != request.walker_id:
            raise ValueError(
                "Can't accept walk request of another dog walker."
            )
        walk_request.status = "ONGOING"
        walk_request.time_start = request.date

        await self.__repository_context.update_walkrequest(
            walk_request, walk_request.id
        )
        await self.__notification_controller._notify_walk_request_accepted(
            walk_request.owner_id, walk_request.walker_id
        )
        return {"success": "The walk request has been accepted."}

    @is_walker
    @authenticated
    async def reject_walk(self, request, walk_request_id: "UUID"):
        """Reject a walk request as a walker."""
        walk_request = await self.__repository_context.read_walkrequest(
            walk_request_id
        )
        if walk_request.status != "PENDING":
            raise ValueError("Can't reject a non-pending walk request")
        if walk_request.walker_id != request.walker_id:
            raise ValueError(
                "Can't accept walk request of another dog walker."
            )
        walk_request.status = "REJECTED"
        walk_request.time_start = request.date

        await self.__repository_context.update_walkrequest(
            walk_request, walk_request.id
        )
        await self.__notification_controller._notify_walk_request_rejected(
            walk_request.owner_id, walk_request.walker_id
        )
        return {"success": "The walk request has been rejected."}

    @is_walker
    @authenticated
    async def complete_walk(self, request, walk_request_id: "UUID"):
        """Complete a walk request as a walker."""
        walk_request = await self.__repository_context.read_walkrequest(
            walk_request_id
        )
        if walk_request.status != "ONGOING":
            raise ValueError("Can't complete a non-ongoing walk request")
        if walk_request.walker_id != request.walker_id:
            raise ValueError(
                "Can't complete walk request of another dog walker."
            )
        walk_request.status = "DONE"
        walk_request.time_end = request.date

        await self.__repository_context.update_walkrequest(
            walk_request, walk_request.id
        )
        return {"success": "The walk request has been completed."}

    @authenticated
    async def set_availability(self, request, availability: bool):
        """Set walker availability to either True or False."""
        user_id = request.user_id
        walkers = await self.__repository_context.search(
            "Walker", f"user_id=={user_id}"
        )
        walker = walkers.first_or_default()
        if walker is None:
            raise Exception("Walker not found.")
        walker.is_available = availability
        return await self.__repository_context.update(
            "Walker", walker, walker.id
        )
