"""Pylinq."""
from py_linq import Enumerable


Enumerable.__len__ = lambda self: self.count()
