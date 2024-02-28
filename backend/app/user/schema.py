from app.core.types import MongoListModel, MongoModel, PydanticObjectId
from typing import List 
from pydantic import SecretStr
from datetime import datetime


class UserSchema(MongoModel):
    id: PydanticObjectId
    username: str
    password: SecretStr
    username: str
    display_name: str    
    telephone: str
    campus: PydanticObjectId
    created_at: datetime   


class StudentSchema(UserSchema):
    wx: str = None
    uni: str = None

class StudentCreateSchema(MongoModel):
    username: str
    password: str
    display_name: str
    telephone: str
    campus: PydanticObjectId
    wx: str
    uni: str

class UserListSchema(MongoListModel):
    __root__: List[UserSchema]