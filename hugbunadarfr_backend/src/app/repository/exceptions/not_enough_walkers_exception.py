"""Error class for when there are too few walkers."""


class NotEnoughWalkersException(Exception):
    """Raised when there are not enough walkers requested."""

    def __init__(self, requested_walkers, true_walker_count, *args, **kwargs):
        """Initialize the exception."""
        super().__init__(*args, **kwargs)
        self.message = "There are not enough walkers in the system.\n" + \
                       f"Available walkers: {true_walker_count}\n" + \
                       f"Requested amount of walkers: {requested_walkers}"
