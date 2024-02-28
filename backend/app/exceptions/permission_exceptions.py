from werkzeug.exceptions import HTTPException
  

class PermissionDenied(HTTPException):
    code = 403

    def __init__(self, message = "Permission denied"):
        self.message = message


