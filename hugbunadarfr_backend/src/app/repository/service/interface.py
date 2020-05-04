"""Interface module.

Launch this module to start the repository!
It will launch a websocket server and you can contact it with any one of the
functions listed in get_available_functions. It expects json of this format:

{
    "command": "create",
    "kwargs": {
        "type": "Dog",
        "model": {
            "name": "Snati",
            "breed": "Poodle",
            "photo_url": "example.com/dogphoto.jpg"
        }
    }
}
"""

import asyncio
import json
import traceback
import websockets
import traceback


from ..repositories import (
    DogRepository, UserRepository, WalkRequestRepository,
    DogOwnerRepository, WalkerRepository, LoginRepository,
    NotificationRepository
)
from ..exceptions.not_found_exception import NotFoundError
from .json_encoder import EntityEncoder, date_hook

walk_request_repo = WalkRequestRepository()
dog_owner_repo = DogOwnerRepository()
user_repo = UserRepository(dog_owner_repo)
dog_repo = DogRepository(dog_owner_repo)
login_repo = LoginRepository(user_repo)
walker_repo = WalkerRepository(walk_request_repo, user_repo)
notification_repo = NotificationRepository()


repos = {
    "Dog": dog_repo,
    "User": user_repo,
    "Walker": walker_repo,
    "WalkRequest": walk_request_repo,
    "DogOwner": dog_owner_repo,
    "Notification": notification_repo,
    "Login": login_repo
}


def get_available_commands():
    """All available commands for the websocket handler."""
    functions = {
        "create": lambda type, model: repos[type].create(model),
        "read": lambda type, id: repos[type].read(id),
        "update": lambda type, model, id: repos[type].update(model, id),
        "delete": lambda type, id: repos[type].delete(id),
        "read_all": lambda type: repos[type].read_all(),
        "search": lambda type, args: repos[type].search(*args),

        # Special actions
        "get_collections": lambda: list(repos.keys()),
        "read_owners_of_dog": lambda id: user_repo.read_owners_of_dog(id),
        "read_dogs_of_owner": lambda id: dog_repo.read_dogs_of_owner(id),
    }
    return functions


def message_handler(request):
    """Handle parsing and execution."""
    command = request["command"]
    kwargs = request.get("kwargs", dict())
    available_commands = get_available_commands()
    try:
        response = available_commands[command](**kwargs)
    except TypeError as e:
        response = {"error": "Bad request: " + str(e)}
        print(traceback.format_exc())
    except NotFoundError as e:
        print(traceback.format_exc())
        response = {"error": "Not found: " + str(e)}
    except KeyError as e:
        response = {"error": "Invalid command parameter: " + str(e)}
    except Exception as e:
        response = {"error": str(e)}
        print(traceback.format_exc())

    return response


async def repository_service(websocket, path):
    """Provide a repository service via websocket."""
    request = await websocket.recv()
    try:
        jsoned_request: dict = json.loads(request, object_hook=date_hook)
        print("< " + request)
        response = message_handler(jsoned_request)
    except json.JSONDecodeError:
        traceback.print_exc()
        response = {
            "error": "The request format is incorrect."
        }

    await websocket.send(json.dumps(response, cls=EntityEncoder))
    print("> " + json.dumps(response, cls=EntityEncoder))


def main():
    """Start the repository websocket interface."""
    url = "localhost"
    port = 8765
    start_server = websockets.serve(repository_service, url, port)

    print("Starting repository service!")
    print(f"Listening on ws://{url}:{port}")

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()


if __name__ == "__main__":
    main()
