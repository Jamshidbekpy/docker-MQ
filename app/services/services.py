from .interfaces import AbstractUserService
from ..schemas.user_schemas import UserIn, UserOut
from ..repositories.repositories import UserRepository
from ..utils import hash_password, verify_password

class UserService(AbstractUserService):
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def register_user(self, user_in: UserIn) -> UserOut:
        hashed_password = hash_password(user_in.password)
        user = self.repo.create_user(user_in.username, hashed_password)
        return UserOut(username=user.username)
    
    def get_user(self, user_in: UserIn) -> UserOut:
        user = self.repo.get_user_by_username(user_in.username)
        if not user:
            raise Exception("User not found")
        if not verify_password(user_in.password, user.hashed_password):
            raise Exception("Invalid password")
        return UserOut(username=user.username)
    
    

