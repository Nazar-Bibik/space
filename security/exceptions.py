class RequestError(Exception):
    http_code = "400"
    http_message = "Bad Request"


class RequestNotFound(Exception):
    http_code = "404"
    http_message = "Not Found"


class NotImplementedError(Exception):
    http_code = "501"
    http_message = "Not Implemented"


class InternalError(Exception):
    http_code = "500"
    http_message = "Internal Server Error"


class UnauthorisedError(Exception):
    http_code = "401"
    http_message = "Unauthorized"

        
class ConnectionTimeOut(Exception):
    http_code = "408"
    http_message = "Request Timeout"


class TooLargeError(Exception):
    http_code = "413"
    http_message = "Entity Too Large"


HTTP_EXCEPTION_ARRAY = (RequestError, RequestNotFound, NotImplementedError, InternalError, UnauthorisedError, ConnectionTimeOut)