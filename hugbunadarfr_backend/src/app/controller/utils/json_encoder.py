"""Encoder."""
import datetime
from dataclasses import asdict, is_dataclass
from json import JSONEncoder
from uuid import UUID
import json
from .enumerable import Enumerable


class EntityEncoder(JSONEncoder):
    """JSON encoding class."""

    def default(self, obj):
        """Encode models as JSON objects."""
        if is_dataclass(obj):
            return asdict(obj)
        if isinstance(obj, UUID) or isinstance(obj, datetime.datetime):
            return str(obj)
        if isinstance(obj, Enumerable):
            return obj.to_list()
        return JSONEncoder.default(self, obj)
