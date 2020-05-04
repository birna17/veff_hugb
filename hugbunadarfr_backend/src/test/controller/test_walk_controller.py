import unittest
from unittest.mock import MagicMock, patch, Mock
import asyncio
from asyncio import coroutine
from py_linq import Enumerable
from uuid import UUID, uuid4
from datetime import datetime
from types import MethodType
from ...app.controller.models import WalkRequest, Login, Walker, Dog
from ...app.controller.utils.request_utils import Request


def async_test(coro):
    def wrapper(*args, **kwargs):
        loop = asyncio.new_event_loop()
        return loop.run_until_complete(coro(*args, **kwargs))
    return wrapper


class TestWalkController(unittest.TestCase):
    """Test the walk controller."""

    def setUp(self):
        """Set up mocks and vars needed for tests."""
        from ...app.controller.controllers import walk_controller
        self.repository_context = MagicMock()
        self.notification_controller = MagicMock()
        self.owner_id = UUID("93226a91-0f3b-4256-9356-8851b735d643")
        self.walker = Walker(
            id=UUID("b0357a3d-9b74-4ba2-b45f-faa288a551b1"),
            is_available=True,
            user_id=uuid4()
        )
        self.dog = Dog(
            id=UUID("2e089ffd-3aca-4ef1-bb11-8dc6d49367b0"),
            name="Woofhound",
            breed="who knows?!",
            photo_url="http://photos.com/image.jpg"
        )
        self.walk_request = WalkRequest(
            owner_id=self.owner_id,
            dog_id=self.dog.id,
            walker_id=self.walker.id,
        )
        self.walk_controller = walk_controller.WalkController(
            self.repository_context, self.notification_controller
        )

    def test_actions(self):
        """Test the actions property of WalkerController."""
        self.assertSetEqual(
            set(self.walk_controller.actions.keys()),
            {
                "get_top_5_walkers", "get_new_top_5_walkers", "order_walker",
                "my_ordered_walks", "accept_walk", "complete_walk",
                "set_availability", "my_walks"
            }
        )
        for val in self.walk_controller.actions.values():
            self.assertIsInstance(val, MethodType)

    @async_test
    async def test_order_walker(self):
        """Test ordering a walker.

        Should succeed.
        """
        async def read_walker(*args, **kwargs):
            return self.walker

        async def read_dog(*args, **kwargs):
            return self.dog

        async def read_dogs_of_owner(*args, **kwargs):
            return Enumerable([self.dog])

        async def create_walkrequest(*args, **kwargs):
            return self.walk_request

        self.repository_context.read_walker = read_walker
        self.repository_context.read_dog = read_dog
        self.repository_context.read_dogs_of_owner = read_dogs_of_owner
        self.repository_context.create_walkrequest = create_walkrequest
        self.notification_controller._notify_walk_request = create_walkrequest
        request = Request(
            user_id=self.owner_id,
            authenticated=True,
            login=Login(user_id=self.owner_id,
                        log_date=datetime.now(),
                        log_expiry_date=datetime.max
                        )
        )
        res = await self.walk_controller.order_walker(
            request, self.walker.id, self.dog.id
        )
        self.assertIsInstance(res, WalkRequest)
        self.assertEqual(res.owner_id, self.owner_id)
        self.assertEqual(res.walker_id, self.walker.id)
        self.assertEqual(res.dog_id, self.dog.id)


if __name__ == '__main__':
    unittest.main()
