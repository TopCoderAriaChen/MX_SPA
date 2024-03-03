from typing import List

from app.campus.model import Campus
from app.core.service import BaseService
from app.course.model import Course
from app.course.schema import CourseCreateSchema, CoursePutSchema, LectureCreateSchema
from app.user.model import Teacher, User
from flask_jwt_extended import get_current_user

class CourseService(BaseService):
    def __init__(self, user: User) -> None:
        super().__init__(CourseService.__name__, user)

    def create_course(self, course: CourseCreateSchema) -> Course:
        self.logger.info("Creating courses")
        Campus.objects(id=course.campus).first_or_404("Campus not exists")
        Teacher.objects(id=course.teacher).first_or_404("Teacher not exists")
        course: CourseCreateSchema = Course(**course.dict())
        return course.save()

    def list_courses(self, campus: str = None, teacher: str = None) -> List[Course]:
        self.logger.info("Fetching courses")
        querys: dict = {}
        if campus is not None:
            querys["campus"] = campus
        if teacher is not None:
            querys["teacher"] = teacher
        return list(Course.objects(**querys))
    
    def get_course(self, course_id: str) -> Course:
        return Course.objects(id=course_id).first_or_404("Course not exists")
    
    def delete_course(self, course_id: str) -> int:
        return Course.objects(id=course_id).delete()

    def update_course(self, course_id: str, course: CoursePutSchema):
        update_dict = course.dict(exclude_none=True, exclude_defaults=True)
        if len(update_dict) == 0:
            return
        Course.objects(id=course_id).first_or_404("Course not exists").update_one(
            **update_dict
        )

    def add_lecture(self, course_id: str, lecture: LectureCreateSchema) -> int:
        course: Course = Course.objects(id=course_id).first_or_404("Course not exists")
        course.update(push__lectures=lecture.dict(exclude_none=True))
        return str(lecture.id)



def course_service():
    return CourseService(get_current_user())