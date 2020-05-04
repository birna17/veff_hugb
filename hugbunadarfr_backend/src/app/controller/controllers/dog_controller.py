"""The Controller for any actions related to dogs.

The only stuff it should need to import are the dog model and related
models as well as some utils. It is not allowed to import another
controller here, or the repository context.
"""

from ..utils.request_utils import authenticated
from ..models.dog_owner import DogOwner
from ..models.dog import Dog
from ..utils.enumerable import Enumerable
from ..exceptions.authentication_error import AuthenticationError
from .controller import Controller


class DogController(Controller):
    """Manage and retrieve data related to dogs."""

    def __init__(self, repository_context: "RepositoryContext"):
        """Init a new DogController, with a given repository_context."""
        super().__init__(repository_context)
        self.__repository_context = repository_context

    @authenticated
    async def get_dog(self, request, dog_id: "UUID") -> "Dog":
        """Get a specific dog by id."""
        dog = await self.__repository_context.read_dog(dog_id)
        return dog

    @authenticated  # Only authenticated users can use this, otherwise error
    async def my_dogs(self, request) -> Enumerable:
        """Get the dogs of the requester.

        Parameter:
        ----------
        self (DogController): The current instance of DogController.
        request (Request): The incoming request object.


        Return:
        ------
        list: The list of all dogs associated with the requestee
        """
        return await self.__repository_context.read_dogs_of_owner(
            request.user_id
        )

    @authenticated
    async def register_dog(self, request, dog) -> "Dog":
        """Register the given Dog object, and associate with this requester."""
        # Add the dog to the repository, and give it a proper ID
        dog = await self.__repository_context.create_dog(dog)

        # Associate the dog with the currently logged in user
        dog_owner = await self.__repository_context.create_dogowner(
            DogOwner(
                owner_id=request.user_id,
                dog_id=dog.id,
            )
        )
        return dog

    @authenticated
    async def update_dog(self, request, dog, dog_id) -> Dog:
        """Update a dog, however you can only update a dog you own."""
        await self._user_owns_dog(request, dog_id)
        return await self.__repository_context.update_dog(dog, dog_id)

    @authenticated
    async def delete_dog(self, request, dog_id):
        """Delete a dog, however you can only delete a dog that you own."""
        await self._user_owns_dog(dog_id)
        return await self.__repository_context.delete_dog(dog_id)

    @authenticated
    async def _user_owns_dog(self, request, dog_id):
        my_dogs = await self.my_dogs(request)
        dog: Dog = my_dogs.where(lambda x: x.id == dog_id).first_or_default()
        if dog is None:
            raise AuthenticationError("You don't own this dog!")

    @property
    def actions(self) -> dict:
        """Read-only property that returns a dict of all functions.

        The key is the function name to expose, and the value is the
        function itself.
        """
        return {
            "my_dogs": self.my_dogs,
            "register_dog": self.register_dog,
            "get_dog": self.get_dog
        }
