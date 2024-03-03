from datetime import datetime

from flask_mongoengine import Document
from mongoengine import (
    CASCADE,
    BooleanField,
    DateTimeField,
    FloatField,
    ReferenceField,
    StringField,
)

from ..course.model import Course
from ..user.model import Student

class Order(Document):
    student = ReferenceField(Student, reverse_delete_rule=CASCADE)
    course = ReferenceField(Course, reverse_delete_rule=CASCADE)
    created_time = DateTimeField(default=datetime.now)
    original_price = FloatField()
    paid = BooleanField(default=False)
    paid_time = DateTimeField()
    paid_comment = StringField()
    paid_price = FloatField()
