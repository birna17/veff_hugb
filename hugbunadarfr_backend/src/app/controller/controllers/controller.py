"""Base controller class."""


class Controller():
    """Base controller."""

    def __init__(self, repository_context: "RepositoryContext"):
        """Init a new Controller, with a given repository_context."""
        self.__repository_context = repository_context

    def get_repository_context(self):
        """Get the controllers repository context."""
        return self.__repository_context
