"""Provides the context to connect to the repository websocket service."""
import websockets
import asyncio
import py_linq
import json
from ..exceptions.repository_error import RepositoryError
from .connection import connection


class RepositoryContext():

    """Provides a facade for the repository.

    Instantiate a RepositoryContext, with the proper URI, and you will be able
    to call it like so:

    ```
    repository_context = RepositoryContext(JsonEncoder, JsonDecoder)
    await repository_context.connect("ws://localhost:8765")
    dogs = await repository_context.Dogs()

    ```

    dogs will be an Enumerable type, that you can query with pylinq.

    ```
    repository_context = RepositoryContext(JsonEncoder, JsonDecoder)
    await repository_context.connect("ws://localhost:8765")
    dog = await repository_context.Dog(dog_id)
    ```

    Will return a specific dog with a specific ID.

    The RepositoryContext will dynamically get any collections offered by the
    repo.
    """

    def __init__(self, JsonDecoder, JsonEncoder, *args, **kwargs):
        """Initialize a new RepositoryContext."""
        self._uri = None
        self.__collections = None
        self.__decoder = JsonDecoder()
        self._encoder = JsonEncoder

    async def connect(self, uri):
        """Connect to a specified URL."""
        self._uri = uri
        self.__collections = await self._get_collections()
        self._generate_collections()
        print(f"Connected to repository at {uri}")

    def _validate_collection(self, collection):
        if collection not in self.__collections:
            raise ValueError(f"{collection} is not a valid collection.")
        return True

    @connection
    def read_owners_of_dog(self, dog_id) -> list:
        """Read the owners of a specified dog."""
        return {
            "command": "read_owners_of_dog",
            "kwargs": {
                "id": user_id
            }
        }

    @connection
    def read_dogs_of_owner(self, user_id) -> list:
        """Read the dogs of a specified user."""
        return {
            "command": "read_dogs_of_owner",
            "kwargs": {
                "id": user_id
            }
        }

    @connection
    def create(self, collection, model):
        """Add a model to the repository of collection."""
        self._validate_collection(collection)
        return {
            "command": "create",
            "kwargs": {
                "type": collection,
                "model": model
            }
        }

    @connection
    def read(self, collection, id):
        """Read the collection item with the specified id."""
        self._validate_collection(collection)
        command = {
            "command": "read",
            "kwargs": {
                "type": collection,
                "id": id,
            }
        }
        return command

    @connection
    def update(self, collection, model, id):
        """Update the model with the specified id in the collection."""
        self._validate_collection(collection)
        return {
            "command": "update",
            "kwargs": {
                "type": collection,
                "model": model,
                "id": id,
            }
        }

    @connection
    def delete(self, collection, id):
        """Delete the item with the specified id from the collection."""
        self._validate_collection(collection)
        return {
            "command": "delete",
            "kwargs": {
                "type": collection,
                "id": id,
            }
        }

    @connection
    def read_all(self, collection):
        """Read all in a specified collection."""
        self._validate_collection(collection)
        return {
            "command": "read_all",
            "kwargs": {
                "type": collection,
            }
        }

    @connection
    def search(self, collection, *parameters):
        """Search in a specified collection, with the given parameters.

        Each parameter should be in a string formmat.
        """
        self._validate_collection(collection)
        return {
            "command": "search",
            "kwargs": {
                "type": collection,
                "args": parameters,
            }
        }

    def _decode(self, request):
        message = json.loads(request)
        if isinstance(message, dict) and "error" in message:
            raise RepositoryError(message)
        decoded_request = self.__decoder(request)
        print("< " + request)
        return decoded_request

    @connection
    def _get_collections(self):
        return {"command": "get_collections"}

    # Dynamically generated functions below allow shortcut access to
    # repository actions.

    def _generate_create(self, collection):
        def create(self, model):
            return {
                "command": "create",
                "kwargs": {
                    "type": collection,
                    "model": model
                }
            }
        return connection(create, self)

    def _generate_read(self, collection):
        def read(self, id):
            return {
                "command": "read",
                "kwargs": {
                    "type": collection,
                    "id": id,
                }
            }
        return connection(read, self)

    def _generate_update(self, collection):
        def update(self, model, id):
            return {
                "command": "update",
                "kwargs": {
                    "type": collection,
                    "model": model,
                    "id": id,
                }
            }
        return connection(update, self)

    def _generate_delete(self, collection):
        def delete(self, id):
            return {
                "command": "delete",
                "kwargs": {
                    "type": collection,
                    "id": id,
                }
            }
        return connection(delete, self)

    def _generate_read_all(self, collection):
        def read_all(self):
            return {
                "command": "read_all",
                "kwargs": {
                    "type": collection,
                }
            }
        return connection(read_all, self)

    def _generate_search(self, collection):
        def search(self, *parameters):
            """Search in a specified collection, with the given parameters.

            Each parameter should be in a string format.
            """
            return {
                "command": "search",
                "kwargs": {
                    "type": collection,
                    "args": parameters,
                }
            }
        return connection(search, self)

    def _generate_collections(self):
        """Generate the CRUD methods for all collections."""
        for collection in self.__collections:
            lo_coll = collection.lower()
            self.__setattr__(
                "create_" + lo_coll, self._generate_create(collection)
            )
            self.__setattr__(
                "read_" + lo_coll, self._generate_read(collection)
            )
            self.__setattr__(
                "update_" + lo_coll, self._generate_update(collection)
            )
            self.__setattr__(
                "delete_" + lo_coll, self._generate_delete(collection)
            )
            self.__setattr__(
                f"read_all_{lo_coll}s", self._generate_read_all(collection)
            )
            self.__setattr__(
                f"search_{lo_coll}s", self._generate_search(collection)
            )
            self.__setattr__(
                collection, self.__getattribute__("read_" + lo_coll)
            )
            self.__setattr__(
                collection + "s",
                self.__getattribute__("read_all_" + lo_coll + "s")
            )


async def main():
    """Testing."""
    from .json_decoder import JsonDecoder
    from .json_encoder import EntityEncoder
    from ..models.dog import Dog

    db_context = RepositoryContext(JsonDecoder, EntityEncoder)
    await db_context.connect("ws://localhost:8765")
    dogs = await db_context.Dogs()
    print(dogs)

    test_dog = Dog(
        name="Snati",
        breed="Hundur",
        photo_url="example.com/image.jpg",
        id=None,
    )
    dog = await db_context.create_dog(test_dog)

    print(dog)

    # dog = await db_context.Dog("wowzers")

    # print(dog)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(
        main()
    )
