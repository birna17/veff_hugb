"""The repository package, containing all of our repos.

You can import each Repo directly from this package like:

from ..repositories import DogRepository, UserRepository
"""
from .repository import Repository
from .dog_repository import DogRepository
from .user_repository import UserRepository
from .walker_repository import WalkerRepository
from .walkrequest_repository import WalkRequestRepository
from .dog_owner_repository import DogOwnerRepository
from .notification_repository import NotificationRepository
from .login_repository import LoginRepository
