import datetime
from app.campus.model import Campus
from flask_restx import Namespace, Resource
from flask import request, jsonify
from flask_jwt_extended import create_access_token, set_access_cookies, jwt_required, current_user

from .model import Admin, Student, Teacher, User, check_password, get_hashed_password
from .schema import AdminCreateSchema, AdminListSchema, AdminSchema, StudentCreateSchema, StudentListSchema, StudentSchema, TeacherCreateSchema, TeacherListSchema, TeacherSchema, UserSchema, UserListSchema
from .service import unauthorized_user_service, user_service
from . import permission_required



auth_api: Namespace = Namespace("auth")

@auth_api.route("")
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


users_api = Namespace("users")

@users_api.route("")
class UsersApi(Resource):
    @permission_required("user_admin")
    def get(self):
        user_type = request.args.get("type", None)
        campus = request.args.get("campus", None)
        if campus is not None:
            campus = Campus.objects(id=campus).first_or_404("Campus not found")

        user_list = user_service().list_users(user_type=user_type, campus=campus)  
        if user_type == "admin":
            return AdminListSchema.from_orm(user_list)
        if user_type == "teacher":
            return TeacherListSchema.from_orm(user_list)
        if user_type == "student":
            return StudentListSchema.from_orm(user_list)
        else:
            return UserListSchema.from_orm(user_list)


students_api = Namespace("students")

@students_api.route("")  
class StudentsApi(Resource):
    def post(self):
        request_data = request.json
        if "campus" not in request_data:
            return {"code": 400, "message": "Campus is not found in the payload"}, 400
        request_data["campus"] = Campus.objects(id=request_data["campus"]).first_or_404(
            "Campus not found"
        )
        student = StudentCreateSchema(**request_data)        
        student = Student(**student.dict())
        student = unauthorized_user_service().register_user(student)
        return StudentSchema.from_orm(student),201 


admins_api = Namespace("admins")

@admins_api.route("")
class AdminApi(Resource):
    @permission_required("sys_owner")
    def post(self):
        request_data = request.json
        if "campus" not in request_data:
            return {"code": 400, "message": "Campus is not found in the payload"}, 400
        request_data["campus"] = Campus.objects(id=request_data["campus"]).first_or_404(
            "Campus not found"
        )
        admin = AdminCreateSchema(**request_data)
        admin = Admin(**admin.dict())
        admin = user_service().register_user(admin)
        return AdminSchema.from_orm(admin), 201


teachers_api = Namespace("teachers")

@teachers_api.route("")
class TeacherApi(Resource):
    @permission_required("sys_owner")
    def post(self):
        request_data = request.json
        if "campus" not in request_data:
            return {"code": 400, "message": "Campus is not found in the payload"}, 400
        request_data["campus"] = Campus.objects(id=request_data["campus"]).first_or_404(
            "Campus not found"
        )
        teacher_schema = TeacherCreateSchema(**request_data)
        teacher = Teacher(**teacher_schema.dict())
        teacher = user_service().register_user(teacher)
        return TeacherSchema.from_orm(teacher), 201
