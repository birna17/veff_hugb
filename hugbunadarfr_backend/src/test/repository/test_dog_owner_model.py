"""Unit test module for dog owner mtehods."""

import unittest
from uuid import uuid4, UUID
from ...app.repository.models.dog_owner import DogOwner


class TestDogOwnerMethods(unittest.TestCase):
    """Test the Dog Owner Metods."""

    def setUp(self):
        """Set up info."""
        self.owner_uuid = uuid4()
        self.dog_uuid = uuid4()
        self.my_dog_owner = DogOwner(
            owner_id=self.owner_uuid, dog_id=self.dog_uuid
        )

    def test_get_owner_id(self):
        """Test get owner id from model."""
        owner = self.my_dog_owner.get_owner_id()
        self.assertEqual(self.owner_uuid, owner)

    def test_get_dog_id(self):
        """Test get dog id from model."""
        dog = self.my_dog_owner.get_dog_id()
        self.assertEqual(self.dog_uuid, dog)

    def test_init_(self):
        """Test create model."""
        self.assertIsNotNone(self.my_dog_owner.get_id())
        self.assertIsInstance(self.my_dog_owner.get_id(), UUID)


if __name__ == '__main__':
    unittest.main()
