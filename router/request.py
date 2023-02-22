from security.exceptions import RequestError
from router.uri import Uri

HTTP_METHOD_TOKENS = ["OPTIONS", "GET", "HEAD", "POST", "PUT", "DELETE", "TRACE", "CONNECT"]

class Request:
    """ This is HTTP request class """
    _method: str
    _uri: Uri
    _version: str
    _header: dict
    _body: bytes

    def __init__(self, data: bytes):
        # Verifying bytes data
        if not data:
            raise RequestError()
        delimiter = bytes("\r\n", "utf-8")
        data_header: bytes = None
        data_body: bytes = None
        if (delimiter + delimiter) not in data:
            data_header == data
        else:
            data_header, data_body = data.split((delimiter + delimiter), 1)
        del data

        self._body = data_body # Setting request body
        del data_body

        # Verifying header bytes
        if not data_header:
            raise RequestError()
        if data_header.startswith(delimiter):
            data_header = data_header[1:]
        try:
            raw_request, raw_header = data_header.decode("utf-8").split("\r\n", 1)
        except ValueError:
            raise RequestError()
        except:
            raise
        del data_header

        # Getting request values
        try:
            request_method, request_uri, request_version = raw_request.split(" ", 3)
        except:
            raise RequestError()
        if request_method not in HTTP_METHOD_TOKENS:
            raise RequestError()
        else:
            self._method = request_method
        self._uri = Uri(request_uri)
        if "HTTP" not in request_version:
            raise RequestError()
        else:
            self._version = request_version

        # Getting header values
        self._header = dict()



    def add_header(self, raw_header: str):
        for header_line in raw_header.replace(" ", "").split("\r\n"):
            name, value = header_line.split(":", 1)
            self._header[name] = value

    
    def print_info(self):
        print(self._method)
        self._uri.print_info()
        print(self._version)
        print(self._header)


    def append_body(self, data: bytes):
        if not data:
            return
        self._body += data

    