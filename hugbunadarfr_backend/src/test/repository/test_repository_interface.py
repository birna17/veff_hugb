"""Test module for the repository interface."""


import unittest
from unittest.mock import MagicMock, patch
from ...app.repository.service import interface
from ...app.repository.models.dog import Dog
from ...app.repository.models.user import User


class TestRepositoryInterface(unittest.TestCase):
    """Test class for repository interface."""

    def setUp(self):
        """Initialize variables before tests."""
        self.dog = Dog(name="Snati", breed="Doberman", photo_url="example.com")
        interface.repos["Dog"] = MagicMock()
        interface.repos["Dog"].delete.return_value = self.dog
        interface.repos["Dog"].read_all.return_value = [self.dog]

    def test_message_handler_given_readAll_request_returns_dog_list(self):
        """Test the message handler for it returning a valid dog list."""
        request = {
            "command": "read_all",
            "kwargs": {"type": "Dog"}
        }
        response = interface.message_handler(request)
        self.assertIsInstance(response, list)
        for item in response:
            self.assertIsInstance(item, Dog)

    def test_message_handler_given_dog_request_should_return_dog(self):
        """Test the message handler for it returning a valid list."""
        request = {
            "command": "read_all",
            "kwargs": {"type": "Dog"}
        }
        response = interface.message_handler(request)
        self.assertIsInstance(response, list)

    def test_message_handler_given_dog_delete_should_return_dog(self):
        """Test the message handler for it deleting and returning the dog."""
        request = {
            "command": "delete",
            "kwargs": {
                "type": "Dog",
                'id': self.dog.id
            }
        }
        response = interface.message_handler(request)
        self.assertIsInstance(response, Dog)
        self.assertEqual(response, self.dog)


if __name__ == '__main__':
    unittest.main()
