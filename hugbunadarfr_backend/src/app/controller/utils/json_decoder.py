"""Decode JSON into the controller models."""
import json
import datetime
from dataclasses_jsonschema import ValidationError
from .enumerable import Enumerable
from uuid import UUID
from ..models import (
    Dog, DogOwner, Login, User, WalkRequest, WalkerReview, Walker,
    Notification
)
import traceback


class JsonDecoder():
    """Decode JSON data into common types with the decode() method."""

    def __call__(self, request):
        """Start the decoding process."""
        request = request.encode('utf-8').decode('utf-8')
        jsoned_request = json.loads(
            request,
            object_hook=self.decode,
            encoding='utf-8',
        )
        if isinstance(jsoned_request, list):
            jsoned_request = Enumerable(jsoned_request)
        return jsoned_request

    @classmethod
    def decode(cls, json_dict):
        """Decode JSON data into common types."""
        json_dict = cls.date_hook(json_dict)
        try:
            model = cls.model_hook(json_dict)
            return model
        except NotAModelError:
            pass
        json_dict = cls.uuid_hook(json_dict)
        return json_dict

    @staticmethod
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

    @staticmethod
    def model_hook(json_dict):
        """Try to convert json values to any model."""
        models = (
            WalkRequest, Notification, Dog, DogOwner, Login, Walker, User,
            WalkerReview
        )

        for model in models:
            try:
                return model.from_dict(json_dict, validate=False)
            except (ValidationError, TypeError, ValueError) as err:
                pass
        raise NotAModelError

    @staticmethod
    def uuid_hook(json_dict):
        """Hook."""
        for (key, value) in json_dict.items():
            try:
                json_dict[key] = UUID(value)
            except (ValueError, AttributeError, TypeError):
                pass
        return json_dict


class NotAModelError(Exception):
    """Raise when json is not a model."""

    pass
