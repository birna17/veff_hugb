"""TestCase class for controller user model."""

from ...app.controller.models.user import User
from ...app.controller.utils.attribute import Attribute
import unittest
from dataclasses_jsonschema import ValidationError


class TestUser(unittest.TestCase):
    """TestCase class for controller dog model."""

    def setUp(self):
        """Set up class."""
        self.username = "username"
        self.password = "123345"
        self.first_name = "johnny"
        self.last_name = "here is"
        self.address = "knoxville 32"
        self.phone_number = "11123313555"
        self.email_address = "jhk@google.com"

    def test_username_attribute(self):
        """Test creating a user with None value in username."""
        try:
            self.username = None
            self.test_user = User(
                username=self.username, password=self.password,
                first_name=self.first_name, last_name=self.last_name,
                address=self.address, phone_number=self.phone_number,
                email_address=self.email_address
            )

        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)

    def test_username2_attribute(self):
        """Test creating a user with empty string."""
        try:
            self.username = ""
            self.test_user = User(
                username=self.username, password=self.password,
                first_name=self.first_name, last_name=self.last_name,
                address=self.address, phone_number=self.phone_number,
                email_address=self.email_address
            )

        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)

    def test_password_attribute(self):
        """Test creating a user with None value in password."""
        try:
            self.password = None
            self.test_user = User(
                username=self.username, password=self.password,
                first_name=self.first_name, last_name=self.last_name,
                address=self.address, phone_number=self.phone_number,
                email_address=self.email_address
            )

        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)

    def test_password2_attribute(self):
        """Test creating a user with length of password smaller than 4 char."""
        try:
            self.password = "122"
            self.test_user = User(
                username=self.username, password=self.password,
                first_name=self.first_name, last_name=self.last_name,
                address=self.address, phone_number=self.phone_number,
                email_address=self.email_address
            )

        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)

    def test_first_name_attribute(self):
        """Test creating a user with None value in first_name."""
        try:
            self.first_name = None
            self.test_user = User(
                username=self.username, password=self.password,
                first_name=self.first_name, last_name=self.last_name,
                address=self.address, phone_number=self.phone_number,
                email_address=self.email_address
            )

        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)

    def test_last_name_attribute(self):
        """Test creating a user with None value in last_name."""
        try:
            self.last_name = None
            self.test_user = User(
                username=self.username, password=self.password,
                first_name=self.first_name, last_name=self.last_name,
                address=self.address, phone_number=self.phone_number,
                email_address=self.email_address
            )

        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)

    def test_address_attribute(self):
        """Test creating a user with None value in address."""
        try:
            self.address = None
            self.test_user = User(
                username=self.username, password=self.password,
                first_name=self.first_name, last_name=self.last_name,
                address=self.address, phone_number=self.phone_number,
                email_address=self.email_address
            )

        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)

    def test_phone_number_attribute(self):
        """Test creating a user with None value in phone_number."""
        try:
            self.phone_number = None
            self.test_user = User(
                username=self.username, password=self.password,
                first_name=self.first_name, last_name=self.last_name,
                address=self.address, phone_number=self.phone_number,
                email_address=self.email_address
            )

        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)

    def test_phone_number2_attribute(self):
        """Test creating a user with nondigit value in phone_number."""
        try:
            self.phone_number = "notAdigit"
            self.test_user = User(
                username=self.username, password=self.password,
                first_name=self.first_name, last_name=self.last_name,
                address=self.address, phone_number=self.phone_number,
                email_address=self.email_address
            )

        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)

    def test_email_address_attribute(self):
        """Test creating a user with None value in email_address."""
        try:
            self.email_address = None
            self.test_user = User(
                username=self.username, password=self.password,
                first_name=self.first_name, last_name=self.last_name,
                address=self.address, phone_number=self.phone_number,
                email_address=self.email_address
            )

        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)

    def test_email_address2_attribute(self):
        """Test creating a user with an invalid email address."""
        try:
            self.email_address = "sdfsdfsff.com"
            self.test_user = User(
                username=self.username, password=self.password,
                first_name=self.first_name, last_name=self.last_name,
                address=self.address, phone_number=self.phone_number,
                email_address=self.email_address
            )

        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)


if __name__ == '__main__':
    unittest.main()
