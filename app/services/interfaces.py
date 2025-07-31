from abc import ABC, abstractmethod
from ..schemas.user_schemas import UserIn, UserOut
class AbstractUserService(ABC):
    @abstractmethod
    def register_user(self, user_in: UserIn) -> UserOut:
        pass
    
    def get_user(self, user_in: UserIn) -> UserOut:
        pass