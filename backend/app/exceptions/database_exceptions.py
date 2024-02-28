from werkzeug.exceptions import HTTPException

class DuplicateRecord(HTTPException):
    code = 409

    def __init__(self, message = "Duplicate Record"):
        self.message = message

 