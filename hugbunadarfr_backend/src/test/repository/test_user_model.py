"""Module for testing user model."""

import unittest
from ...app.repository.models.user import User
from ...app.repository.models.entity import Entity


class TestUserInterface(unittest.TestCase):
    """Test the user model functons."""

    def setUp(self):
        """Set up the user to be tested."""
        self.my_user = User(
            username="palmi18",
            password="123",
            first_name="Palmi",
            last_name="Runarsson",
            address="Heima 123",
            phone_number="1234567",
            email_address="besti@best.com")

    def test_get_username(self):
        """Test get."""
        userName = self.my_user.get_username()
        self.assertEqual(userName, "palmi18")

    def test_get_password(self):
        """Test get."""
        userPassword = self.my_user.get_password()
        self.assertEqual(userPassword, "123")

    def test_get_first_name(self):
        """Test get."""
        userFirstName = self.my_user.get_first_name()
        self.assertEqual(userFirstName, "Palmi")

    def test_get_last_name(self):
        """Test get."""
        userLastName = self.my_user.get_last_name()
        self.assertEqual(userLastName, "Runarsson")

    def test_get_fullname(self):
        """Test Fill name."""
        fullName = self.my_user.get_full_name()

    def test_get_address(self):
        """Test get."""
        userAddress = self.my_user.get_address()
        self.assertEqual(userAddress, "Heima 123")

    def test_get_phone(self):
        """Test get."""
        userPhone = self.my_user.get_phone_number()
        self.assertEqual(userPhone, "1234567")

    def test_get_email(self):
        """Test get."""
        userEmail = self.my_user.get_email_address()
        self.assertEqual(userEmail, "besti@best.com")


if __name__ == '__main__':
    unittest.main()
