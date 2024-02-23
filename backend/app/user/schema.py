from app.core.types import MongoModel, PydanticObjectId
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

