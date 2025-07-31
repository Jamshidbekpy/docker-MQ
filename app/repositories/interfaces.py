# repository interface
from abc import ABC, abstractmethod
from ..models import User

class AbstractUserRepository(ABC):
    @abstractmethod
    def create_user(self, username: str, hashed_password: str) -> User:
        pass

    @abstractmethod
    def get_user_by_username(self, username: str) -> User:
        pass
