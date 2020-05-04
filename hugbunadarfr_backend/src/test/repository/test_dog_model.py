"""Dog method tests."""
import unittest
from ...app.repository.models.dog import Dog


class TestDogMethods(unittest.TestCase):
    """TestCase class for dog methods."""

    def setUp(self):
        """Set up class."""
        url = "https://www.foxsumo.com/wp-content/uploads/2019/08/Pug.jpg"
        self.my_dog = Dog(name="Kormákur", breed="Pug", photo_url=url)

    def test_set_name(self):
        """Test name setting."""
        self.my_dog.set_name("Mr. Dog")
        self.assertEqual(self.my_dog.name, "Mr. Dog")

    def test_set_breed(self):
        """Test setting breed."""
        self.my_dog.set_breed("Chihuahua")
        self.assertEqual(self.my_dog.breed, "Chihuahua")

    def test_set_photo_url(self):
        """Test setting photo url."""
        self.my_dog.set_photo_url("fotbolti.net")
        self.assertIsInstance(self.my_dog.photo_url, str)

    def test_get_name(self):
        """Test getting name."""
        dogName = self.my_dog.get_name()
        self.assertEqual(dogName, "Kormákur")

    def test_get_breed(self):
        """Test getting breed."""
        dogBreed = self.my_dog.get_breed()
        self.assertEqual(dogBreed, "Pug")

    def test_get_photo_url(self):
        """Test getting photo url."""
        url = self.my_dog.get_photo_url()
        self.assertEqual(self.my_dog.photo_url, url)

    def test_creating_dog_with_kwargs(self):
        """Test creating a dog with keyword arguments, the normal way."""
        dog = Dog(
            name="Mjá", breed="Poodle", photo_url="example.com/image.jpg"
        )
        self.assertIsInstance(dog, Dog)
        try:
            self.assertEqual(dog.name, "Mjá")
        except AttributeError:
            self.fail("dog.name raised AttributeError. " +
                      "It should exist, but does not")
        try:
            self.assertEqual(dog.breed, "Poodle")
        except AttributeError:
            self.fail("dog.breed raised AttributeError. " +
                      "It should exist, but does not")
        try:
            self.assertEqual(dog.photo_url, "example.com/image.jpg")
        except AttributeError:
            self.fail("dog.photo_url raised AttributeError. " +
                      "It should exist, but does not")

    def test_creating_dog_with_args(self):
        """Test creating a dog with normal arguments, the lesser used way.

        However it should be possible. There is a chance that this will
        not works due to how dataclasses behave with required and
        optional arguments.
        """
        dog = Dog("Voffi Góði", "Great Dane", "example.com/image2.png")
        self.assertIsInstance(dog, Dog)
        try:
            self.assertEqual(dog.name, "Voffi Góði")
        except AttributeError:
            self.fail("dog.name raised AttributeError. " +
                      "It should exist, but does not")
        try:
            self.assertEqual(dog.breed, "Great Dane")
        except AttributeError:
            self.fail("dog.breed raised AttributeError. " +
                      "It should exist, but does not")
        try:
            self.assertEqual(dog.photo_url, "example.com/image2.png")
        except AttributeError:
            self.fail("dog.photo_url raised AttributeError. " +
                      "It should exist, but does not")


if __name__ == '__main__':
    unittest.main()
