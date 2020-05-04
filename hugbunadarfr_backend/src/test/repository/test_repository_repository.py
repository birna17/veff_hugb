"""Module for testing the repository."""

import uuid
import unittest
from unittest.mock import MagicMock
from ...app.repository.repositories.repository import Repository
from ...app.repository.models.dog import Dog


class TestRepository(unittest.TestCase):
    """Test class for repository."""

    def setUp(self):
        """Set up variables before tests."""
        self.dog = Dog(
            name="snati",
            override_id="9123588c-1797-49b8-80a4-b47bd301dbe8",
            breed="poodle",
            photo_url="example.com/mypic.png",
        )
        self.test_repo = Repository(Dog, "Dogs")
        self.test_repo._Repository__REPO = {
            uuid.UUID("9123588c-1797-49b8-80a4-b47bd301dbe8"): self.dog
        }

    def test_create(self):
        """Test creating a new object and inserting it to the repo."""
        new_id = uuid.uuid4()
        new_dog = self.test_repo.create(
            {"name": "mummi", "override_id": new_id,
             "breed": "border", "photo_url": "example.com/mypic.png"}
        )
        self.assertIsInstance(new_dog, Dog)
        self.assertEqual(new_dog.name, "mummi")

    def test_deleting_dog(self):
        """Test deleting something from the repo."""
        dog = self.test_repo.delete("9123588c-1797-49b8-80a4-b47bd301dbe8")
        self.assertIsInstance(dog, Dog)

    def test_read_dog(self):
        """Test reading a dog from the repo."""
        dog = self.test_repo.read("9123588c-1797-49b8-80a4-b47bd301dbe8")
        self.assertEqual(dog, self.dog)


if __name__ == '__main__':
    unittest.main()
