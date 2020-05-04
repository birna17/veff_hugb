"""TestCase class for login model."""

from ...app.repository.models.login import Login
import unittest
from uuid import UUID
import datetime
from dataclasses_jsonschema import ValidationError


class TestLogin(unittest.TestCase):
    """Testing login."""

    def setUp(self):
        """Set up class."""

        self.current_user_id = "828ad1d3-8f09-4d35-9c22-0a5eb367240a"
        self.current_time = datetime.datetime.today()
        self.the_login = Login(user_id=self.current_user_id,
                               log_date=self.current_time)

    def test_get_user_id(self):
        """Test get user id."""
        login_user_id = self.the_login.get_user_id()
        self.assertEqual(login_user_id, self.current_user_id)

    def test_get_login_token(self):
        """Test get login token."""
        login_token = self.the_login.get_token()
        self.assertIsInstance(login_token, UUID)

    def test_get_date(self):
        """Test get date."""
        the_date = self.the_login.get_date()
        self.assertIsInstance(the_date, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
