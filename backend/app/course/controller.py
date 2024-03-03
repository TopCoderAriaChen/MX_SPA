from flask import request
from flask_jwt_extended import jwt_required
from flask_restx import Namespace, Resource
from flask_pydantic import validate
from app.course.schema import CourseCreateSchema, CourseListSchema, CourseSchema
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

@api.route("/<string:course_id>")
class CourseApi(Resource):

    @permission_required("course_admin")
    def get(self, course_id):
        return CourseSchema.from_orm(course_service().get_course(course_id))

    @permission_required("course_admin")
    def delete(self, course_id):
        return course_service().delete_course(course_id), 200
