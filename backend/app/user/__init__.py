from .model import User

def register_user_lookup(jwt):
    def user_lookup_callback(_jwt_header, jwt_data):
        identity = jwt_data["sub"]

        return User.objects(id=identity).first_or_404(message="User not found")

    jwt.user_lookup_loader(user_lookup_callback)
