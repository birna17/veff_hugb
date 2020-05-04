"""Test module for walker methods."""

import unittest
from ...app.repository.models.dog import Dog
from ...app.repository.repositories.dog_repository import DogRepository


class TestWalkerMethods(unittest.TestCase):
    """Test all methods in walker model."""

    def setUp(self):
        """Set up test walker methods."""
        url = "https://www.foxsumo.com/wp-content/uploads/2019/08/Pug.jpg"
        self.my_dog = Dog(name="Kormákur", breed="Pug", photo_url=url)


if __name__ == '__main__':
    unittest.main()
