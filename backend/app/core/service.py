from flask import request
from app.log import CorrelationLogger

class BaseService:
    def __init__(self, service_name, user=None, parent_logger=None) -> None:
        if parent_logger is None:
            self.logger: CorrelationLogger = request.logger.getChild(service_name)
        else:
            self.logger: CorrelationLogger = parent_logger.getChild(service_name)
        
        if user is not None:
            self.logger.base = {**self.logger.base, "user": user.id}
        