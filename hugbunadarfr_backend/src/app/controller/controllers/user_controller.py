"""The Controller for any action related to the user."""
from datetime import datetime, timedelta

from ..utils.request_utils import authenticated
from ..models.walker import Walker
from ..models.login import Login
from ..models.user import User
from ..utils.repository_context import RepositoryContext
from ..utils.enumerable import Enumerable
from dataclasses import fields
from ..exceptions.authentication_error import AuthenticationError
from .controller import Controller


class UserController(Controller):
    """Manage and retrieve data related to users (and walkers)."""

    def __init__(self, repository_context: RepositoryContext):
        """Init a new UserController, with a given repository_context."""
        super().__init__(repository_context)
        self.__repository_context = repository_context

    @property
    def actions(self) -> dict:
        """Read-only property that returns a dict of all functions.

        The key is the function name to expose, and the value is the
        function itself.
        """
        return {
            "login": self.login,
            "register": self.register,
            "logout": self.logout,
            "become_walker": self.become_walker,
        }

    async def login(self, request, username: str, password: str) -> "UUID":
        """Add user to login repo."""
        # Idea is to first search all users with the given username and see if
        # the password matches.
        # Then we need to create a new login object, insert it into the repo
        # and ultimately return to the user an access_token string (eg a uuid)

        # Get the user list with the given username
        users: Enumerable = await self.__repository_context.search_users(
            f"username=={username}"
        )
        # Get the first or defult value
        user: User = users.first_or_default()
        # if no user is found raise exception
        if user is None:
            # No user with this username found
            raise Exception("Username not found")

        # Check is password matches username.
        # Then create the login entry
        if user.password == password:
            user_login = await self.__repository_context.create_login(
                Login(
                    user_id=user.id,
                    log_date=datetime.now(),
                    log_expiry_date=datetime.now() + timedelta(7)
                )
            )
            return {"access_token": user_login.log_token}
        else:
            # Username does not match password
            raise Exception("Login failed")

    async def register(self, request, user: User):
        """Create a new user."""
        # register the user, provided there is no other user with the same
        # username.

        # Check is username exists

        if not isinstance(user, User):
            user_fields = [f.name for f in fields(User) if f.name != "id"]
            raise Exception(f"Invalid fields for registration.\n " +
                            f"Please include values for: {user_fields}")

        username_exist = await self.__repository_context.search_users(
            f"username=={user.username}"
        )
        if username_exist:
            raise Exception("Username is taken")

        # Add the user to the repository, and give him an ID
        new_user = await self.__repository_context.create_user(user)

        # Check if user exists again, if he does then success!
        username_exist = self.__repository_context.search_users(
            f"id=={new_user.id}"
        )
        # give message if failed or successful
        if username_exist:
            return {
                "success": "You can use the 'login' command " +
                "to get an access token."
            }
        else:
            raise Exception("Registration failed.")

    @authenticated
    async def logout(self, request):
        """Remove the current user from the login repo."""
        # Login id by the authenticated token
        logins: Enumerable = await self.__repository_context.search_logins(
            f"log_token=={request.access_token}"
        )
        # Get the first or defult value
        login = logins.first_or_default()
        # Delete the given login entry with the given id
        await self.__repository_context.delete_login(login.id)

    @authenticated
    async def become_walker(self, request):
        """Take the user that is logged in and add him to the walkers repo."""
        walkerExist = await self.__repository_context.search(
            "Walker",
            f"id=={request.user_id}"
        )
        if len(walkerExist) > 0:
            raise Exception("You are already a Walker")
        return await self.__repository_context.create_walker(
            Walker(
                user_id=request.user_id,
                is_available=False,
            )
        )

    async def get_authentication(self, access_token):
        """Get the user ID of an authenticated user.

        NOT A METHOD TO BE USED BY INTERFACE DIRECTLY.
        """
        login = await self.__repository_context\
            .search_logins(f"log_token=={access_token}")
        login = login.first_or_default()
        if login is not None:
            return login
        else:
            raise AuthenticationError
