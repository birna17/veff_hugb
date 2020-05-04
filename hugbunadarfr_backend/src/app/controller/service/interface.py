"""The controller interface service.

The UI will be able to request things through this service. It uses accepts
JSON commands in a structure similar to the repository service.

There are many commands that you can use with the controller interface.
You can see all of them with this websocket command:

{
    "command": "get_actions",
    "kwargs": {}
}

To register use a command like this:

{
    "command": "login",
    "kwargs": {
        "username": "my_username",
        "password": "my_pass"
    }
}

You'll get back a string like this (assuming it works):
"dadf215f-fcaf-458b-90bd-7b27c6300fdb"

This is your authorization token. Use it from now on in all your requests to
access most other functions. For example, if you want to see your dogs use:

{
    "command": "my_dogs"
    "access_token": "dadf215f-fcaf-458b-90bd-7b27c6300fdb"
}
"""

import asyncio
import json
import traceback
import websockets

from ..utils.repository_context import RepositoryContext
from ..utils.json_decoder import JsonDecoder
from ..utils.json_encoder import EntityEncoder
from ..controllers.dog_controller import DogController
from ..controllers.user_controller import UserController
from ..controllers.walk_controller import WalkController
from ..controllers.notification_controller import NotificationController
from ..exceptions.repository_error import RepositoryError
from ..exceptions.authentication_error import AuthenticationError
from . import process_request
from ..utils.bad_request_util import make_error_message


repository_context = RepositoryContext(JsonDecoder, EntityEncoder)
dog_controller = DogController(repository_context)
user_controller = UserController(repository_context)
notification_controller = NotificationController(repository_context)
walk_controller = WalkController(repository_context, notification_controller)


def get_available_commands():
    """All available commands for the websocket handler."""
    actions = dict()
    actions.update(dog_controller.actions)
    actions.update(user_controller.actions)
    actions.update(walk_controller.actions)
    actions.update(notification_controller.actions)

    async def get_actions(request):
        return list(actions.keys())

    async def help(request):
        return __doc__
    actions["get_actions"] = get_actions
    actions["help"] = help
    return actions


async def message_handler(request):
    """Handle parsing and execution."""
    command = request["command"]

    kwargs = request.get("kwargs", dict())
    request_obj = await process_request.process(request, user_controller)
    available_commands = get_available_commands()
    try:
        response = await available_commands[command](
            request_obj, **kwargs
        )
    except RepositoryError as e:
        response = {"error": "RepositoryError: " + str(e)}
        traceback.print_exc()
    except AuthenticationError as e:
        response = {
            "error": "AuthenticationError: " + str(e),
            "info": "You need to be logged in and send the 'access_token' " +
                    'you got to use this method.'
        }
        traceback.print_exc()
    except TypeError as e:
        fun = available_commands[command]
        response = {
            "error": "Bad request: " + str(e),
            "info": make_error_message(fun)
        }
        traceback.print_exc()
    except KeyError as e:
        response = {
            "error": "Invalid command parameter: " + str(e),
            "info": "Send the 'help', or 'get_actions' commands to see more"
        }
        traceback.print_exc()
    except Exception as e:
        response = {"error": str(e)}
        traceback.print_exc()
    return response


async def controller_service(websocket, path):
    """Provide a repository service via websocket."""
    request = await websocket.recv()
    try:
        json_decode = JsonDecoder()
        jsoned_request: dict = json_decode(request)
        print("< " + request)
        response = await message_handler(jsoned_request)
    except json.JSONDecodeError:
        traceback.print_exc()
        response = {
            "error": "The request format is incorrect."
        }
    if response is None:
        response = {
            "success": None,
            "info": "This command does not return anything."
        }
    await websocket.send(json.dumps(response, cls=EntityEncoder))
    print("> " + json.dumps(response, cls=EntityEncoder))


def main():
    """Start the controller websocket interface."""
    url = "localhost"
    port = 8766
    repository_uri = "ws://localhost:8765"
    start_server = websockets.serve(controller_service, url, port)

    try:
        asyncio.get_event_loop().run_until_complete(
            repository_context.connect(repository_uri)
        )
    except OSError:
        print("ERROR STARTING SERVICE! \n"
              f"EXPECTED REPOSITORY SERVICE AT {repository_uri}")
        return

    print("Starting controller service!")
    print(f"Listening on ws://{url}:{port}")

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()


if __name__ == "__main__":
    main()
