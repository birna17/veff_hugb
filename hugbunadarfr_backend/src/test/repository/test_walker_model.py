"""Module for testing walker methods."""
import unittest
from ...app.repository.models.walker import Walker
import uuid


class TestWalkerMethods(unittest.TestCase):
    """Test all methods in walker model."""

    def setUp(self):
        """Initialize walker object before testing."""
        self.my_walker = Walker(
            override_id="b76debee-16b3-4f9e-ba3c-68b1402901b2",
            is_available=True,
        )

    def test_set_availablility(self):
        """Test setting availability."""
        self.my_walker.set_availability(False)
        self.assertEqual(self.my_walker.is_available, False)

    def test_get_availability(self):
        """Test getting availability."""
        self.assertEqual(self.my_walker.get_availability(), True)


if __name__ == '__main__':
    unittest.main()
