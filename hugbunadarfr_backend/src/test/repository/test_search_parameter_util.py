"""Search parameter utility tests."""
import unittest
from ...app.repository.utils.search_parameter import search_parameter
from types import FunctionType


class TestSearchParameterUtil(unittest.TestCase):
    """TestCase class for dog methods."""

    def test_search_param_success(self):
        """Test using the search parameter, success case."""
        operators = ["==", "!=", "<", ">", "<=", ">="]
        try:
            for op in operators:
                res = search_parameter(f"test{op}value")
                self.assertIsInstance(res, FunctionType)
        except Exception as err:
            self.fail(str(err))

    def test_search_param_failure(self):
        """Test using the search parameter, failure case."""
        invalid = ["nothing", None, 1, 0.3]
        for item in invalid:
            with self.assertRaises(TypeError):
                search_parameter(item)


if __name__ == '__main__':
    unittest.main()
