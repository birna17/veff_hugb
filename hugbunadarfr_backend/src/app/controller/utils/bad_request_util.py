"""Utility for creating useful error messages for interface."""

import inspect
import inspect
from typing import Callable
import sys


def make_error_message(func: Callable) -> str:
    """Make an error message detailing function attributes."""
    try:
        tb_frame = sys.exc_info()[-1]
        while tb_frame.tb_next is not None:
            tb_frame = tb_frame.tb_next
        func = tb_frame.tb_frame.f_locals["func"]
    except (KeyError, TypeError, AttributeError):
        pass
    message = f"{func.__name__}: {func.__doc__}\n"
    message += f"{func.__name__} takes these arguments:"
    argspec = inspect.signature(func)
    for key, val in argspec.parameters.items():
        if key in ("self", "request"):
            continue
        annotation = val.annotation
        if annotation == inspect._empty:
            annotation = "json"
        elif isinstance(annotation, type):
            annotation = annotation.__name__
        message += f"\n\t{key}: {annotation}"
        if val.default != inspect._empty:
            message += f", default={val.default}"
    return message


if __name__ == "__main__":
    def decorator(func):
        """Test decorator."""
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)
        return wrapper

    @decorator
    def a(test_b: str):
        """Call the A method."""
        pass

    try:
        a(b="wow")
    except TypeError as err:
        print(make_error_message(a))
