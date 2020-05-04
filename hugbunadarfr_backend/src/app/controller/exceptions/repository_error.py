"""Error class for when repository queries fail."""


class RepositoryError(Exception):
    """Raised when repository query fails."""

    def __init__(self, message, *args, **kwargs):
        """Initialize RepositoryError."""
        super().__init__(*args, **kwargs)
        self.message = str(message)

    def __str(self):
        return self.message
