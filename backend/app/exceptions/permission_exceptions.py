from werkzeug.exceptions import HTTPException


class PermissionDenied(HTTPException):
    code = 403

    def __init__(self, message="Permission Denied") -> None:
        self.description = message
