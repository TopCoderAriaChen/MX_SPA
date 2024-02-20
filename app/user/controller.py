import datetime
from flask_restx import Namespace, Resource
from flask import request, jsonify
from flask_jwt_extended import create_access_token, set_access_cookies, jwt_required, current_user

from .model import User, check_password, get_hashed_password
from .schema import UserSchema


auth_api: Namespace = Namespace("auth")

@auth_api.route("/")
class UserAuthInfo(Resource):
    @jwt_required()
    def get(self):
        return UserSchema.from_orm(current_user)



@auth_api.route("/login")
class Login(Resource):
    def post(self):
        username = request.json.get("username")
        password = request.json.get("password")
        if not username or not password:
            return {"message": "username or password is missing"}, 400

        user = User.objects(username=username).first_or_404(message="User not found")
        if not check_password(password, user.password):
            return {"message": "Username or Password is incorrect"}, 401

        jwt_token = create_access_token(
            identity = str(user.id), expires_delta = datetime.timedelta(days=30)
        )

        response =  jsonify({"access_token": jwt_token})
        set_access_cookies(response, jwt_token)
        return response
