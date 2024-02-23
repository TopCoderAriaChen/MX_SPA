import datetime
import json

from pydantic import BaseModel, SecretStr

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        elif isinstance(obj, SecretStr):
            return None
        elif isinstance(obj, BaseModel):
            return obj.dict(exclude_defaults=True)
        else:
            return super().default(obj)
