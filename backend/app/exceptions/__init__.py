from flask import request
from mongoengine import ValidationError as MongoengineValidationError
from pydantic import ValidationError as PydanticValidationError
from werkzeug.exceptions import HTTPException
from flask_jwt_extended.exceptions import NoAuthorizationError

from .permission_exceptions import PermissionDenied

def register_resources_exception_handler(api):
    @api.errorhandler(NoAuthorizationError)
    def handle_authorization_error(e: NoAuthorizationError):
        request.logger.error(getattr(e, "description", str(e)))
        return {"code": 401, "message": getattr(e, "description", str(e))}, 401

    @api.errorhandler(PermissionDenied)
    def handle_permission_denied(e: PermissionDenied):
        request.logger.error(getattr(e, "description", str(e)))
        return {
            "code": 403, 
            "message": getattr(e, "description", str(e))
        }, 403

    @api.errorhandler(HTTPException)
    def handle_default_http_exception(e: HTTPException):
        return {
            "code": e.code,
            "message": getattr(e, "description", str(e)),
        }, e.code

    @api.errorhandler(PydanticValidationError)
    def handle_pydantic_value_error(e: PydanticValidationError):
        return {"code": 400, "message": "Validation Error", "errors": e.errors()}, 400

    @api.errorhandler(MongoengineValidationError)
    def handle_mongo_value_error(e: MongoengineValidationError):
        return {
            "code": 400,
            "message": "Model error: " + e.message,
            "field": e.field_name,
        }, 400

    @api.errorhandler(Exception)
    def handle_default_exception(e: Exception):
        request.logger.error(str(e))
        return {"code": 500, "message": "Internal server errror"}, 500
