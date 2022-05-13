
# ArgumentValueError
class ResponseError(ValueError):
    def __init__(self, message):
        super().__init__("Error " + str(message))


class APIKeyError(ValueError):
    def __init__(self, message):
        super().__init__(message)
