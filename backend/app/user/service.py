from typing import List

from flask_jwt_extended import get_current_user

from app.core.service import BaseService
from app.user.model import User


class UserService(BaseService):
    def __init__(self, user):
        super().__init__(UserService.__name__, user)
    
    def list_users(self) -> List[User]:
        self.logger.info("Fetching users")
        return list(User.objects())
    

def user_service():
    return UserService(get_current_user())

def unauthorized_user_service():
    return UserService()
  