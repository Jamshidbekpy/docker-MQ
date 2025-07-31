# repository implementation
from sqlalchemy.orm import Session
from .interfaces import AbstractUserRepository
from ..models import User

class UserRepository(AbstractUserRepository):
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, username: str, hashed_password: str) -> User:
        user = User(username=username, hashed_password=hashed_password)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_user_by_username(self, username: str) -> User:        
        return self.db.query(User).filter(User.username == username).first()