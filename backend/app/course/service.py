from typing import List
import uuid

from app.campus.model import Campus
from app.core.service import BaseService
from app.course.model import Course, Lecture
from app.course.schema import CourseCreateSchema, CoursePutSchema, LectureCreateSchema, LecturePutSchema
from app.user.model import Teacher, User
from flask_jwt_extended import get_current_user

class CourseService(BaseService):
    def __init__(self, user: User) -> None:
        super().__init__(CourseService.__name__, user)

    def get_course_query(self, **kwargs):
        if self.user._cls == "User.Admin" and "course_admin" in self.user.permissions:
            return Course.objects(**kwargs)
        if self.user._cls == "User.Teacher":
            return Course.objects(teacher=self.user, **kwargs)
        else:
            return Course.objects(enrolled_students=self.user, **kwargs)

    def create_course(self, course: CourseCreateSchema) -> Course:
        self.logger.info("Creating course")
        Campus.objects(id=course.campus).first_or_404("Campus not exists")
        Teacher.objects(id=course.teacher).first_or_404("Teacher not exists")
        course: CourseCreateSchema = Course(**course.dict())
        return course.save()

    def list_courses(self, campus: str = None, teacher: str = None) -> List[Course]:
        self.logger.info("Fetching courses")
        querys = {}
        if campus is not None:
            querys["campus"] = campus
        if teacher is not None:
            querys["teacher"] = teacher
        return list(Course.objects(**querys))

    def get_course(self, course_id: str) -> Course:
        return self.get_course_query(id=course_id).first_or_404("Course not exists")
    
    def delete_course(self, course_id: str) -> int:
        self.logger.info("Deleting course")
        return Course.objects(id=course_id).delete()

    def update_course(self, course_id: str, course: CoursePutSchema):
        self.logger.info("Updating course")
        update_dict = course.dict(exclude_none=True, exclude_defaults=True)
        if len(update_dict) == 0:
            return
        Course.objects(id=course_id).first_or_404("Course not exists").update(
            **update_dict
        )
 

    def add_lecture(self, course_id: str, lecture: LectureCreateSchema) -> int:
        lecture.id = uuid.uuid4()
        self.logger.info("Adding lecture")
        course: Course = Course.objects(id=course_id).first_or_404("Course not exists")
        course.update(push__lectures=lecture.dict(exclude_none=True))
        return str(lecture.id)

    def list_lectures(self, course_id: str) -> List[Lecture]:
        self.logger.info("Listing lectures")
        return Course.objects(id=course_id).first_or_404("Course not exists").lectures
    
    def delete_lecture(self, course_id: str, lecture_id: str) -> int:
        self.logger.info("Deleting lecture")
        return (
            Course.objects(id=course_id)
            .filter(lectures__id=lecture_id)
            .update_one(pull__lectures__id=lecture_id)
        )
    
    def update_lecture(self, course_id: str, lecture_id: str, lecture: LecturePutSchema) -> int:
        self.logger.info("Updating lecture")
        update_action = {
            f"set__lectures__S__{key}": value
            for key, value in lecture.dict(exclude_defaults=True).items()
        }
        return (
            Course.objects(id=course_id)
            .filter(lectures__id=lecture_id)
            .update_one(**update_action)
        )


def course_service():
    return CourseService(get_current_user())