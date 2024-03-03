import datetime
import json
from uuid import UUID

from pydantic import BaseModel, SecretStr

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        elif isinstance(obj, SecretStr):
            return None
        elif isinstance(obj, BaseModel):
            return obj.dict(exclude_defaults=True)
        elif isinstance(obj, UUID):
            return str(obj)
        else:
            return super().default(obj)
