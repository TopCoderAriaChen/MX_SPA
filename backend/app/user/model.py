import base64
import hashlib
from app.user.schema import AdminSchema, StudentSchema, TeacherSchema, UserSchema
import bcrypt
from datetime import datetime

from flask_mongoengine import Document
from mongoengine import StringField, ReferenceField, CASCADE, ListField, DateTimeField
from app.campus.model import Campus

def get_hashed_password(plain_text_password):
    return bcrypt.hashpw(
        base64.b64encode(hashlib.sha256(plain_text_password.encode("utf-8")).digest()),
        bcrypt.gensalt(),
    ).decode("utf-8")

def check_password(plain_text_password, hashed_password):
    return bcrypt.checkpw(
        base64.b64encode(hashlib.sha256(plain_text_password.encode("utf-8")).digest()),
        hashed_password.encode("utf-8"),
    )


class User(Document):
    username = StringField(required=True, unique=True, max_length=36)
    password = StringField(required=True)
    display_name = StringField()
    telephone = StringField()
    campus = ReferenceField(Campus, reverse_delete_rule=CASCADE)
    created_at = DateTimeField(default = datetime.utcnow())
    meta = {
        "allow_inheritance":True, 
        "indexes": ["username", "campus"],
    }

    def to_dict(self):
        return UserSchema.from_orm(self).dict()


class Student(User):
    wx = StringField()
    uni = StringField()

    def to_dict(self):
        return StudentSchema.from_orm(self).dict()


class Admin(User):
    permissions = ListField(StringField(), required=True, default=[])

    def to_dict(self):
        return AdminSchema.from_orm(self).dict()


class Teacher(User):
    abn = StringField(max_length=20)

    def to_dict(self):
        return TeacherSchema.from_orm(self).dict()