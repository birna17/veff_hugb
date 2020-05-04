"""The repository module for the base class Repository."""

import typing
import json
import uuid
from py_linq import Enumerable
from dataclasses import fields, MISSING
from ..data.data_provider import data
from ..exceptions.not_found_exception import NotFoundError
from ..exceptions.bad_model_exception import BadModelError
from ..utils.search_parameter import search_parameter


class Repository():
    """The Repository base class.

    Acts as a database and json interpreter.
    """

    def __init__(self, model: typing.Callable, collection_name: str):
        """Create a new repository for a given model type to store entities."""
        self.__MODEL = model
        self.__NAME = collection_name
        self.__REPO: dict = data[self.__NAME]

    def create(self, model: dict) -> "Entity":
        """Add a new entity to the repo. Takes a dictionary model.

        Raises BadModelError if input model does not conform to entity.
        """
        entity = self.__input_model_to_entity(
            model, model.get("override_id", None)
        )
        self.__add_to_repo(entity)
        return entity

    def read(self, id: uuid.UUID) -> "Entity":
        """Read and return an entity with the given ID.

        Raises NotFoundError if it does not exist.
        """
        if not isinstance(id, uuid.UUID):
            try:
                id = uuid.UUID(str(id))
            except ValueError:
                raise NotFoundError(id, self.__NAME)
        try:
            return self.__REPO[id]
        except KeyError:
            raise NotFoundError(id, self.__NAME)

    def update(self, model: dict, id: int):
        """Update an existing entity with the given id with a model dict."""
        entity = self.__input_model_to_entity(model)
        old_entity = self.read(id)
        for field in fields(self.__MODEL):
            if field.name == "id":
                continue
            value = entity.__getattribute__(field.name)
            old_entity.__setattr__(field.name, value)
        return old_entity

    def delete(self, id) -> "Entity":
        """Delete and return an entity with the given ID from the repo."""
        return self.__pop_from_repo(id)

    def read_all(self):
        """Read all entities in the collection and return them as a list."""
        return list(dict(self.__REPO).values())

    def search(self, *args):
        """Search for matching entities.

        The function should be provided with a list of arguments that the
        entity should match.
        Each argument should be a string following this pattern:
        [field][!=|==|<|>|<=|>=][value]

        Examples:
        --------
        "name==John"
        "age>=18"

        If given multiple arguments, it will apply the 'and' operation eg
        where .search("name==John", "age>=18") would yield a John who is at
        least 18.
        """
        entities = Enumerable(self.read_all())
        for arg in args:
            entities = entities.where(search_parameter(arg))
        return entities

    def __input_model_to_entity(self, model: dict, id=None) -> "Entity":
        """Convert an input model dictionary to an entity."""
        cleaned_model = dict()
        for field in fields(self.__MODEL):
            if field.name == "id":
                continue
            if field.name in model:
                value = model[field.name]
                if value is None:
                    if field.default is not MISSING:
                        value = field.default
                    elif field.default_factory is not MISSING:
                        value = field.default_factory()
                elif not isinstance(value, field.type):
                    value = field.type(value)
                cleaned_model[field.name] = value
        if id is not None:
            cleaned_model["override_id"] = id
        if "id" in cleaned_model:
            del cleaned_model["id"]
        try:
            return self.__MODEL(**cleaned_model)
        except Exception as err:
            raise BadModelError(self.__MODEL, list(model.keys()))

    def __add_to_repo(self, entity: "Entity"):
        """Append new and replace old entities."""
        self.__REPO[entity.get_id()] = entity

    def __pop_from_repo(self, id: uuid.UUID):
        """Pop the specified item from the repo."""
        item = self.read(id)
        return self.__REPO.pop(item.id)
