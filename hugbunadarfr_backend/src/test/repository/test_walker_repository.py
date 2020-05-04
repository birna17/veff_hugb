"""Walker repository method tests."""

import unittest
from unittest.mock import MagicMock
from ...app.repository.service import interface
from ...app.repository.repositories.walker_repository import WalkerRepository
from ...app.repository.models.walker import Walker
from ...app.repository.models.user import User
from ...app.repository.repositories.user_repository import UserRepository
from ...app.repository.repositories import WalkRequestRepository


class TestWalkerRepository(unittest.TestCase):
    """Test the become_a_walker function."""

    def setUp(self):
        """Create a user repository and adds a potential walker."""
        self.user_repo = UserRepository(None)
        self.my_user = self.user_repo.create(
            {"username": "palmi18",
             "password": "123", "first_name": "Palmi",
             "last_name": "Runarsson", "address": "Heima 123",
             "phone_number": "1234567", "email_address": "besti@best.com"
             }
        )

    def test_become_a_walker(self):
        """Test become a walker."""
        walk_request_repo = WalkRequestRepository()
        walker_repo = WalkerRepository(walk_request_repo, self.user_repo)
        walker_repo.set_as_walker(self.my_user.id)
        walker = walker_repo.read(self.my_user.id)
        self.assertIsInstance(walker, Walker)


if __name__ == '__main__':
    unittest.main()
