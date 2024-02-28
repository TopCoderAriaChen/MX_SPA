from typing import List
from app.exceptions.database_exceptions import DuplicateRecord

from flask_jwt_extended import get_current_user

from app.core.service import BaseService
from app.user.model import User, get_hashed_password
from mongoengine.errors import NotUniqueError

class UserService(BaseService):
    def __init__(self, user):
        super().__init__(UserService.__name__, user)
    
    def list_users(self) -> List[User]:
        self.logger.info("Fetching users")
        return list(User.objects())
    
    def register_user(self, user: User):
        try:
            user.password = get_hashed_password(user.password)
            user.save()
            return user
        except NotUniqueError:
            raise DuplicateRecord("User already exists")


def user_service():
    return UserService(get_current_user())

def unauthorized_user_service():
    return UserService(None)
  