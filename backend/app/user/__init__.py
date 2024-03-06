from .model import User

import functools

from flask_jwt_extended import current_user, jwt_required
from app.exceptions.permission_exceptions import PermissionDenied

from .model import Admin, Student, Teacher, User  

def register_user_lookup(jwt) -> None:
    def user_lookup_callback(_jwt_header, jwt_data):
        identity = jwt_data["sub"]
        return User.objects(id=identity).first_or_404(message="User not found")
    
    jwt.user_lookup_loader(user_lookup_callback)

def permission_required(permission=None):
    def wrapper(func):
        @jwt_required()
        @functools.wraps(func)
        def decorator(*arg, **kwargs):
            if current_user._cls == "User.Admin":
                if permission is None or permission in current_user.permissions:
                    return func(*arg, **kwargs)
                else:
                    raise PermissionDenied(f"Permission '{permission}' is required")
            raise PermissionDenied()        
        return decorator
    return wrapper