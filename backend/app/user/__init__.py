import functools
from flask_jwt_extended import current_user, jwt_required
from .model import User

def register_user_lookup(jwt):
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
                    return {
                        "code": 403,
                        "message": f"Permission '{permission}' is required",
                    }, 403
            return {
                "code": 403,
                "message": "Permission denied",
            }, 403
        return decorator
    return wrapper
