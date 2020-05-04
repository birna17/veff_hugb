"""Error class for when repository items are not found."""


class NotFoundError(Exception):
    """Raised when repository lookup fails."""

    def __init__(self, id, repositoryName, *args, **kwargs):
        """Initialize NotFoundError."""
        super().__init__(*args, **kwargs)
        self.message = f"ID {id} not found in {repositoryName} repository."

    def __str__(self):
        """Get error message."""
        return str(self.message)
