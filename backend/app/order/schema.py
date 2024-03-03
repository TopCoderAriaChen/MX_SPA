from datetime import datetime
from typing import List

from pydantic import BaseModel

from app.core.types import AllOptional, MongoListModel, MongoModel, PydanticObjectId

class OrderSchema(MongoModel):
    id: PydanticObjectId
    student: PydanticObjectId
    course: PydanticObjectId
    created_time: datetime
    original_price: float
    paid: bool = False
    paid_time: datetime = None
    paid_comment: str = None
    paid_price: float = None

class OrderCreateSchema(MongoModel):
    student: PydanticObjectId
    course: PydanticObjectId
    original_price: float = None
    paid: bool = False
    paid_time: datetime = None
    paid_comment: str = None
    paid_price: float = None

class OrderPutSchema(OrderSchema, metaclass=AllOptional):
    pass

class OrderPaymentSchema(BaseModel):
    paid: bool = True
    paid_time: datetime = datetime.utcnow()
    paid_comment: str = "No comment"
    paid_price: float = None

class OrderListSchema(MongoListModel):
    __root__: List[OrderSchema]
