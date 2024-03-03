from flask import request
from flask_jwt_extended import jwt_required
from flask_restx import Namespace, Resource
from flask_pydantic import validate
from app.course.schema import CourseCreateSchema, CourseListSchema
from app.course.service import course_service
from app.user import permission_required

api = Namespace("courses")

@api.route("")
class CoursesApi(Resource):
    @jwt_required()
    def get(self):
        campus = request.args.get("campus", None)
        teacher = request.args.get("teacher", None)
        course_list = course_service().list_courses(campus=campus, teacher=teacher)
        return CourseListSchema.from_orm(course_list), 200

    @permission_required("course_admin")
    @validate()
    def post(self, body: CourseCreateSchema):
        return str(course_service().create_course(body).id), 201
