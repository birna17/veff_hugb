"""TestCase class for controller dog model."""
from ...app.controller.models.dog import Dog
from ...app.controller.utils.attribute import Attribute
import unittest
from dataclasses_jsonschema import ValidationError


class TestDog(unittest.TestCase):
    """TestCase class for controller dog model."""

    def setUp(self):
        """Set up class."""
        self.url = "https://www.foxsumo.com/wp-content/uploads/2019/08/Pug.jpg"
        self.name = "nonni"
        self.breed = "collie"

    def test_name_attribute(self):
        """Test creating a dog with number for its name."""
        name = 999
        self.assertRaises(
            ValidationError,
            Dog,
            name=name, breed=self.breed, photo_url=self.url
        )

    def test_name_length(self):
        """Test creating a dog with name shorter than 3 letters."""
        name = "er"
        self.assertRaises(
            ValidationError,
            Dog,
            name=name, breed=self.breed, photo_url=self.url
        )

    def test_breed_attribute(self):
        """Test creating a dog with None value in breed."""
        name = self.name
        breed = None
        self.assertRaises(
            ValidationError,
            Dog,
            name=name, breed=breed, photo_url=self.url
        )

    def test_breed_lengthL(self):
        """Test creating a dog with breed shorter than 3 letters."""
        name = self.name
        breed = "Ro"
        self.assertRaises(
            ValidationError,
            Dog,
            name=name, breed=breed, photo_url=self.url
        )

    def test_url_attribute(self):
        """Test creating a dog with None value in url."""
        name = self.name
        breed = self.breed
        photo_url = None
        self.assertRaises(
            ValidationError,
            Dog,
            name=name, breed=breed, photo_url=photo_url
        )


if __name__ == '__main__':
    unittest.main()
