"""User repo method tests."""
import unittest
from ...app.repository.models.user import User
from ...app.repository.repositories.user_repository import UserRepository


class TestUserRepository(unittest.TestCase):
    """Test the user read_owner_of_dogs functons."""

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

    def test_read_owner_of_dogs(self):
        """Testing read owner of dogs."""
        pass
