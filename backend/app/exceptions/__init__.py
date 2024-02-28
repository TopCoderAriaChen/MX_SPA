from flask import request
from werkzeug.exceptions import HTTPException

from .permission_exceptions import PermissionDenied

def register_resources_exception_handler(api):
    @api.errorhandler(PermissionDenied)
    def handle_permission_denied(e: PermissionDenied):
        request.logger.error(e.message)
        return {"code": 403, "message": e.message}, 403

    @api.errorhandler(HTTPException)
    def handle_default_http_exception(e: HTTPException):
        return {
            "code": e.code,
            "message": e.message is not None and e.message or e.description,
        }