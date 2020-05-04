"""Testing class for the Entity class."""

import unittest
from uuid import UUID
from ...app.repository.models.entity import Entity
from ...app.repository.models.dog import Dog


class TestEntityModel(unittest.TestCase):
    """Test the Entity interface.

    Includes several test cases to test the unique functions of Entity
    in order to maximize test coverage.
    """

    def setUp(self):
        """Create a test entity."""
        self.id = "828ad1d3-8f09-4d35-9c22-0a5eb367240a"
        self.entity = Dog(
            override_id=self.id
        )

    def test_get_id(self):
        """Test getting the Entity ID, its type and value."""
        self.assertIsInstance(self.entity.get_id(), UUID)
        self.assertEqual(self.id, str(self.entity.get_id()))
        self.assertEqual(UUID(self.id), self.entity.get_id())

    def test_create(self):
        """Test creating an entity, both with and without an override_id."""
        entity1 = Entity()
        self.assertIsInstance(entity1, Entity)

    # These next functions test the == operator of Entities
    def test_equality_for_self(self):
        """The entity is equal to itself."""
        self.assertEqual(self.entity, self.entity)

    def test_equality_for_other_entity_with_same_id(self):
        """The entity is equal to another entity with the same ID."""
        other = Entity(override_id=self.id)
        self.assertEqual(self.entity, other)

    def test_equality_for_other_entity_with_different_id(self):
        """The entity is not equal to another entity with a different id."""
        other_id = "828ad1d3-8f09-4d35-9c22-00000000000a"
        other = Entity(override_id=other_id)
        self.assertNotEqual(self.entity, other)

    def test_equality_against_string_equal_to_id(self):
        """The entity is equal to a string with it's id."""
        self.assertEqual(self.entity, self.id)

    def test_equality_against_string_not_equal_to_id(self):
        """The entity is not equal to a string with a different id."""
        other_id = "828ad1d3-8f09-4d35-9c22-00000000000a"
        self.assertNotEqual(self.entity, other_id)


if __name__ == '__main__':
    unittest.main()
