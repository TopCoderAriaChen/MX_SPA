import uuid
from datetime import datetime
from flask_mongoengine import Document
from mongoengine import (
    CASCADE,
    DateTimeField,
    EmbeddedDocument,
    EmbeddedDocumentListField,
    FloatField,
    ListField,
    ReferenceField,
    StringField,
    UUIDField,
)
from app.campus.model import Campus
from app.user.model import Student, Teacher

class LectureAttachment(EmbeddedDocument):
    name = StringField()
    type = StringField()
    filename = StringField()
    bucket_url = StringField()

class Lecture(EmbeddedDocument):
    id = UUIDField(required=True, binary=False, default=uuid.uuid4)
    title = StringField(required=True)
    streaming_url = StringField(required=True)
    recording_url = StringField(required=True)
    scheduled_at = DateTimeField(required=True)
    attachments = EmbeddedDocumentListField(LectureAttachment, default=[])

class Course(Document):
    name = StringField(required=True, max_length=200)
    uni_course_code = StringField(required=True, max_length=200)
    description = StringField(required=True, max_length=200)
    teacher = ReferenceField(Teacher, required=True, reverse_delete_rule=CASCADE)
    campus = ReferenceField(Campus, required=True, reverse_delete_rule=CASCADE)
    created_time = DateTimeField(default=datetime.utcnow)
    publish_time = DateTimeField(default=datetime.utcnow)
    original_price = FloatField(default=0.0)
    cover_image = StringField(default="")
    lectures = EmbeddedDocumentListField(Lecture, default=[])
    enrolled_students = ListField(
        ReferenceField(Student, reverse_delete_rule=CASCADE, default=[])
    )

    meta = {"indexes": ["uni_course_code", "teacher", "campus"]}

Student.register_delete_rule(Course, "enrolled_courses", CASCADE)
