from bson import ObjectId
from flask_mongoengine import Document
from mongoengine.base.datastructures import BaseList, LazyReference
from typing import Any
from pydantic import BaseModel
from pydantic.main import ModelMetaclass
from typing import Optional

class PydanticObjectId(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if ObjectId.is_valid(v):
            return PydanticObjectId(v)
        if isinstance(v, LazyReference) or isinstance(v, Document):
            return PydanticObjectId(v.id)
        print(type(v))
        raise ValueError("Invalid ObjectId")

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class MongoModel(BaseModel):
    @classmethod
    def _get_value(cls, v:Any, to_dict: bool, **kwargs: Any) -> Any:
        if to_dict and type(v) is BaseList:
            return list(v)
        return super()._get_value(v, to_dict=to_dict, **kwargs)
    
    class Config:
        orm_mode = True


class MongoListModel(MongoModel):
    def dict(self, *args, **kwargs):
        return super().dict(*args, **kwargs)["__root__"]


class AllOptional(ModelMetaclass):
    def __new__(self, name, bases, namespace, **kwargs):
        annotations = namespace.get("__annotations__", {})
        for base in bases:
            annotations.update(base.__annotations__)
        for field in annotations:
            if not field.startswith("__"):
                annotations[field] = Optional[annotations[field]]
        namespace["__annotations__"] = annotations
        return super().__new__(self, name, bases, namespace, **kwargs)
