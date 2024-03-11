from datetime import datetime
from typing import List

from pydantic import SecretStr, validator

from app.core.types import AllOptional, MongoListModel, MongoModel, PydanticObjectId
from app.course.schema import CourseBasicInfoSchema


class UserCampusSchema(MongoModel):
    id: PydanticObjectId
    name: str


class UserSchema(MongoModel):
    id: PydanticObjectId
    username: str
    password: SecretStr
    display_name: str
    telephone: str
    campus: UserCampusSchema
    created_at: datetime
    user_type: str

    @validator("user_type")
    def extract_user_type(cls, v):
        return v.split(".")[-1].lower()

    class Config:
        orm_mode = True
        fields = {"user_type": "_cls"}


class UserCreateSchema(MongoModel):
    username: str
    password: str
    display_name: str
    telephone: str
    campus: PydanticObjectId


class UserPutSchema(MongoModel, metaclass=AllOptional):
    password: str
    display_name: str
    telephone: str


class StudentSchema(UserSchema):
    wx: str = None
    uni: str = None
    enrolled_courses: List[CourseBasicInfoSchema]


class StudentCreateSchema(UserCreateSchema):
    wx: str
    uni: str


class StudentPutSchema(UserPutSchema, metaclass=AllOptional):
    wx: str
    uni: str


class AdminSchema(UserSchema):
    permissions: List[str]


class AdminCreateSchema(UserCreateSchema):
    permissions: List[str]


class AdminPutSchema(UserPutSchema, metaclass=AllOptional):
    permissions: List[str]


class TeacherSchema(UserSchema):
    abn: str = None


class TeacherCreateSchema(UserCreateSchema):
    abn: str = None


class TeacherPutSchema(UserPutSchema, metaclass=AllOptional):
    abn: str = None


class UserListSchema(MongoListModel):
    __root__: List[UserSchema]


class AdminListSchema(MongoListModel):
    __root__: List[AdminSchema]


class StudentListSchema(MongoListModel):
    __root__: List[StudentSchema]


class TeacherListSchema(MongoListModel):
    __root__: List[TeacherSchema]
