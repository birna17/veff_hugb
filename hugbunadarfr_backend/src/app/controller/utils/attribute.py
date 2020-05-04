"""A way to create custom properties for python dataclasses.

Property attribute functions take three arguments
    - obj, the object the attribute belongs to
    - field, the field object of the attribute (see dataclasses)
    - value, the value to set
"""

from typing import Callable
from dataclasses import fields, Field
import validators
from validators import ValidationFailure, validator
from dataclasses_jsonschema import ValidationError


class Attribute():
    """Class that helps to create value-checking attributes."""

    @staticmethod
    def _attribute(function, field_name, *args, **kwds):
        def check(f):
            def new_f(*args2, **kwds2):
                all_fields = fields(args2[0])
                for field in all_fields:
                    if field.name == field_name:
                        function(args2[0], field, args2[1], *args)
                        break
                else:
                    raise ValidationError(
                        f"{args2[0]} object has no field {field_name}."
                    )
                return f(*args2, **kwds2)
            return new_f
        return check

    @classmethod
    def _is_set(cls, value):
        """Internally used to see if a particular value has been set."""
        return value is not None and not isinstance(value, property)

    @staticmethod
    def _failed(obj, field, msg):
        """Raise exception as validation failed."""
        raise ValidationError(f"Property '{field.name}' in " +
                              f"{object.__repr__(obj)} should {msg}.")

    @classmethod
    def new(cls, field_name: str,
            *attr_functions: Callable, default=None) -> property:
        """Create a new property with a custom attribute functions."""

        def getter(self):
            if not isinstance(self.__dict__[field_name], property):
                return self.__dict__[field_name]
            return default

        def setter(self, value):
            self.__dict__[field_name] = value

        for item in reversed(attr_functions):
            setter = cls._attribute(item, field_name)(setter)

        return property(getter, setter)

    # Actual attributes
    @classmethod
    def required(cls, obj: object, field: Field, value):
        """Validate the value to exist, and not be None."""
        if not cls._is_set(value):
            raise ValidationError(
                f"Property '{field.name}' in {object.__repr__(obj)}"
                f" is required, but is not set"
            )

    @classmethod
    def min_length(cls, min):
        """Validate a minimum length for a field."""
        def check(obj: object, field: Field, value):
            if not cls._is_set(value):
                return
            if len(value) < min:
                msg = f"be of at least length {min} but is only {len(value)}."
                cls._failed(obj, field, msg)
        return check

    @classmethod
    def max_length(cls, max):
        """Validate a maximum length for a field."""
        def check(obj: object, field: Field, value):
            if not cls._is_set(value):
                return
            if len(value) > max:
                msg = f"be of at most length {min} but is {len(value)}."
                cls._failed(obj, field, msg)
        return check

    @classmethod
    def enforce_type(cls, obj: object, field: Field, value):
        """Validate the type of a field to follow its type hint."""
        if not isinstance(value, field.type) and cls._is_set(value):
            msg = f" be of type: {field.type.__name__} but is: " + \
                  f"{type(value).__name__}"
            cls._failed(obj, field, msg)

    @classmethod
    def length_between(cls, min=None, max=None):
        """Validate that a value is between to extremes."""
        def check(obj: object, field: Field, value):
            if not cls._is_set(value):
                return
            try:
                return validators.between(len(value), min, max)
            except validators.ValidationFailure as err:
                raise ValidationError(str(err))
        return check

    @classmethod
    def url(cls, obj: object, field: Field, value):
        """Validate a url."""
        if not cls._is_set(value):
            return
        try:
            return validators.url(value)
        except validators.ValidationFailure as err:
            raise ValidationError

    @classmethod
    def email(cls, obj: object, field: Field, value):
        """Validate an email."""
        if not cls._is_set(value):
            return
        if validators.email(value):
            return True
        else:
            raise ValidationError("an invalid email was set")

    @classmethod
    def phone_number(cls, obj: object, field: Field, value):
        """Validate a phone number.

        There are a few rules a phone number must follow
        1. It is a string.
        2. It is between 7 and 15 digits in length.
        3. It can include dashes or spaces.
        4. Other than dashes or spaces, it should only include digits.
        5. It can be None, unless it has the required attribute additionally.
        """
        if not cls._is_set(value):
            return

        if not isinstance(value, str):
            cls._failed(
                obj, field, "should be a string as it's a phone number."
            )
        value = value.replace("-", "").replace(" ", "").strip()
        try:
            validators.length(value, 7, 15)
        except ValidationFailure:
            msg = "contain between 7 to 15 digits as it is a phone number"
            cls._failed(obj, field, msg)
        for char in value:
            # if not char.is_digit():
            if not char.isdigit():
                msg = "contain only digits as it is a phone number"
                cls._failed(obj, field, msg)

    # Further ideas for validation properties
    # - regex, force a field to follow a regex pattern string
