"""Error class for when repository items are not found."""


class BadModelError(Exception):
    """Raised when failed to create a model."""

    def __init__(self, entity_cls, fields, *args, **kwargs):
        """Initialize NotFoundError."""
        super().__init__(*args, **kwargs)
        self.message = f"Unable to create {entity_cls.__name__} with " \
            f"given fields {fields}. Needs " \
            f"{entity_cls.__dict__.get('__annotations__')}"

    def __str__(self):
        """Get error message."""
        return str(self.message)
