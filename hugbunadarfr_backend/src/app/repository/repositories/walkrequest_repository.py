"""WalkRequest module."""

from ..models.walk_request import WalkRequest
from .repository import Repository


class WalkRequestRepository(Repository):
    """WalkRequestRepository class."""

    def __init__(self):
        """Initialize WalkRequestRepository."""
        model = WalkRequest
        name = "WalkRequests"
        super().__init__(model=model, collection_name=name)
