"""Error class for when authentication is not sufficient."""

_default_message = "You need to be authenticated to do this action."


class AuthenticationError(Exception):
    """Raised when authentication is not sufficient."""

    def __init__(self, message=_default_message, *args, **kwargs):
        """Initialize AuthenticationError."""
        super().__init__(*args, **kwargs)
        self.message = str(message)

    def __str__(self):
        """To string."""
        return self.message
