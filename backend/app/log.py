from datetime import datetime
import logging
import os
import uuid
import json

from flask import Flask, request
from pythonjsonlogger import jsonlogger 

class Correlation:
    def __init__(self):
        self.id = uuid.uuid4()
        self.timestamp = datetime.utcnow()

    def to_dict(self):
        return{
            "correlationId":str(self.id),
            "correlationTimestamp":self.timestamp.isoformat(),
        }
    
    def get_duration_in_seconds(self):
        elapsed = datetime.utcnow() - self.timestamp
        return round(elapsed.microseconds / 1000 / 1000, 3)
    
class CorrelationLogger:
    def __init__(self, logger, correlation):
        self.logger = logger
        self.base = correlation

    @staticmethod
    def _decorate(base, extra):
        return {**base, **extra}

    def info(self, message, extra={}):
        self.logger.info(message, extra=self._decorate(self.base, extra))

    def warning(self, message, extra={}):
        self.logger.warning(message, extra=self._decorate(self.base, extra))

    def error(self, message, extra={}):
        self.logger.error(message, extra=self._decorate(self.base, extra))

    def debug(self, message, extra={}):
        self.logger.debug(message, extra=self._decorate(self.base, extra))

    def getChild(self, name):
        return CorrelationLogger(self.logger.getChild(name), self.base)


def config_log(app: Flask):
    log_path = os.path.join(app.root_path, "logs")
    if not os.path.exists(log_path):
        os.makedirs(log_path)

    file_handler = logging.FileHandler(f"{log_path}/default.log")
    json_formatter = jsonlogger.JsonFormatter(
        "%(asctime)s %(levelname)s %(module)s %(message)s"
    )
    file_handler.setFormatter(json_formatter) 
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.DEBUG)

    # Config request logger
    @app.before_request
    def before_request():
        request.correlation = Correlation()
        request.logger = CorrelationLogger(
            app.logger, request.correlation.to_dict()
        )
        extra = {
            "x-request-id": request.headers.get("x-request-id"),
            "method": request.method,
            "path": request.path,
            "querys": json.dumps(request.args),
        }
        request.logger.info("request", extra)  
    
    @app.after_request
    def after_request(response):
        extra = {
            "x-request-id": request.headers.get("x-request-id"),
            "method": request.method,
            "path": request.path,
            "statusCode": response.status_code,
            "duration": request.correlation.get_duration_in_seconds(),
        }
        request.logger.info("response", extra)
        return response

    return app
