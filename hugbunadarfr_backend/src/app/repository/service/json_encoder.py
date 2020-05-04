"""Module for encoding json."""

import datetime
from dataclasses import asdict, is_dataclass
from json import JSONEncoder
from uuid import UUID
import json
from py_linq import Enumerable


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


def date_hook(json_dict):
    """Try to convert json values to datetime."""
    for (key, value) in json_dict.items():
        try:
            json_dict[key] = datetime.datetime.strptime(
                value, "%Y-%m-%dT%H:%M:%S")
        except (ValueError, TypeError):
            pass
        try:
            json_dict[key] = datetime.datetime.strptime(
                value, "%Y-%m-%d %H:%M:%S.%f")
        except (ValueError, TypeError):
            pass
    return json_dict
