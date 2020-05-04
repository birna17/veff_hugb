"""testing walker controll model."""
import websockets
import asyncio
import threading
import unittest

from ...app.controller.utils.json_decoder import JsonDecoder
from ...app.controller.utils.json_encoder import EntityEncoder


class TestRepositoryContext(unittest.TestCase):
    """TestCase class for controller dog model."""

    def setUp(self):
        """Set up class."""
        from ...app.controller.utils import connection as conn

        def connection(func, self=None):
            def wrapper(self, *args, **kwargs):
                return func(self, *args, **kwargs)

            def instance_wrapper(*args, **kwargs):
                return func(self, *args, **kwargs)
            if self is not None:
                return instance_wrapper
            return wrapper

        conn.connection = connection

        from ...app.controller.utils.repository_context import (
            RepositoryContext
        )
        self.__repository_context = RepositoryContext(
            JsonDecoder, EntityEncoder
        )
        self.__repository_context._RepositoryContext__collections = [
            "Test1", "Test2"
        ]
        self.__repository_context._generate_collections()

    def test_create(self):
        """Test the create method."""
        item = self.__repository_context.create("Test1", {"test": None})
        expected = {
            'command': 'create',
            'kwargs': {
                'model': {'test': None},
                'type': 'Test1'
            }
        }
        self.assertDictEqual(item, expected)

    def test_create_test1(self):
        """Test the create metod."""
        item = self.__repository_context.create_test1({"test": None})
        expected = {
            'command': 'create',
            'kwargs': {
                'model': {'test': None},
                'type': 'Test1'
            }
        }
        self.assertDictEqual(item, expected)

    def test_read(self):
        """Test the read metod."""
        item = self.__repository_context.read("Test1", "test")
        expected = {
            'command': 'read',
            'kwargs': {
                'id': "test",
                'type': 'Test1'
            }
        }
        self.assertDictEqual(item, expected)

    def test_update(self):
        """Test the update metod."""
        item = self.__repository_context.update("Test1", {"test": None}, "owu")
        expected = {
            'command': 'update',
            'kwargs': {
                'model': {'test': None},
                'id': "owu",
                'type': 'Test1'
            }
        }
        self.assertDictEqual(item, expected)

    def test_delete(self):
        """Test the delete metod."""
        item = self.__repository_context.delete("Test1", "idtest")
        expected = {
            'command': 'delete',
            'kwargs': {
                'id': "idtest",
                'type': 'Test1'
            }
        }
        self.assertDictEqual(item, expected)

    def test_search(self):
        """Test the search metod."""
        item = self.__repository_context.search(
            "Test2", "this=='that'", "my_test==1")
        expected = {
            'command': 'search',
            'kwargs': {
                'args': ("this=='that'", 'my_test==1'),
                'type': 'Test2'
            }
        }
        self.assertDictEqual(item, expected)

    def test_search_test2(self):
        """Test the search metod with 2 args."""
        item = self.__repository_context.search(
            "Test2", "test==test", "test2 >= 2")
        expected = {
            'command': 'search',
            'kwargs': {
                'type': 'Test2',
                'args': ('test==test', 'test2 >= 2',)
            }
        }
        self.assertDictEqual(item, expected)

    def test_read_all(self):
        """Test the read_all metod."""
        item = self.__repository_context.read_all("Test2")
        expected = {
            'command': 'read_all',
            'kwargs': {
                'type': 'Test2'
            }
        }
        self.assertDictEqual(item, expected)


if __name__ == '__main__':
    unittest.main()
