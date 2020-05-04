"""testing walker controll model."""
from ...app.controller.models.walker import Walker
from ...app.repository.models.user import User
from ...app.controller.utils.attribute import Attribute
import unittest
from dataclasses_jsonschema import ValidationError
import uuid


class TestWalker(unittest.TestCase):
    """TestCase class for controller dog model."""

    def setUp(self):
        """Set up class."""
        pass

    def test_walker_isavailable(self):
        """Testing walker availability with None in is_available."""
        try:
            self.is_available = None
            self.test_walker_isavailable = Walker(
                is_available=self.is_available
            )
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)

    def test_walker2_isavailable(self):
        """Testing walker availability with True in is_available."""
        try:
            self.is_available = True
            self.test_walker_isavailable = Walker(
                is_available=self.is_available
            )
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)

    def test_walker3_isavailable(self):
        """Testing walker availability with False in is_available."""
        try:
            self.is_available = False
            self.test_walker_isavailable = Walker(
                is_available=self.is_available
            )
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)


if __name__ == '__main__':
    unittest.main()
