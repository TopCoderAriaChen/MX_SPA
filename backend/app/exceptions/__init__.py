from flask import request
from werkzeug.exceptions import HTTPException
from .permission_exceptions import PermissionDenied

    
def register_resources_exception_handler(api):
    @api.errorhandler(PermissionDenied)
    def handle_permission_denied(e: HTTPException):
        request.logger.error(e.message)
        return {"code": 403, "message": e.message}, 403


        