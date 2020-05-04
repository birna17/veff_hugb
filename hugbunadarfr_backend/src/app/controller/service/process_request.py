"""Take a request dictionary and return a request object.

It also has some other nice features such as identifying the user.
"""

from ..utils.request_utils import Request
from ..controllers.user_controller import UserController
from ..exceptions.authentication_error import AuthenticationError


async def process(request: dict, user_controller: UserController):
    """Convert a request dict to a request object."""
    new_request = Request()
    new_request.access_token = request.get("access_token")
    try:
        new_request.login = await user_controller.get_authentication(
            new_request.access_token
        )
        new_request.user_id = new_request.login.user_id
        new_request.authenticated = True
    except AuthenticationError:
        new_request.authenticated = False

    return new_request
