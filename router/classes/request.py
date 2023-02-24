from security.exceptions import RequestError, NotImplementedError
from router import Uri

HTTP_METHOD_TOKENS = ["OPTIONS", "GET", "HEAD", "POST", "PUT", "DELETE", "TRACE", "CONNECT"]

class Request:
    """ This is HTTP request class """
    _method: str
    _uri: Uri
    _version: str
    _header: dict
    _body: bytes
    _no_ending: bool
    _buffer: bytes


    def __init__(self, data: bytes):
        self._method = None
        self._uri = None
        self._version = None
        self._header = dict()
        self._body = bytes("", "utf-8")
        self._no_ending = True
        self._buffer = bytes("", "utf-8")
        if not data:
            return
        self.add_data(data)
        # # Verifying bytes data
        # if not data:
        #     raise RequestError()
        # delimiter = bytes("\r\n", "utf-8")
        # data_header: bytes = None
        # data_body: bytes = None
        # self._no_ending = False
        # if (delimiter + delimiter) not in data:
        #     data_header == data
        #     self._no_ending = True
        # else:
        #     data_header, data_body = data.split((delimiter + delimiter), 1)

        # self._body = data_body # Setting request body

        # # Verifying header bytes
        # if not data_header:
        #     raise RequestError()
        # if data_header.startswith(delimiter):
        #     data_header = data_header[1:]
        # try:
        #     raw_request, raw_header = data_header.decode("utf-8").split("\r\n", 1)
        # except ValueError:
        #     raise RequestError()
        # except:
        #     raise

        # # Getting header values
        # self._header = dict()
        # self.add_header(raw_header)


    def add_data(self, data: bytes):
        if not data:
            raise RequestError
        if not self._no_ending:
            self.append_body(data)
            return
        
        delimiter = bytes("\r\n", "utf-8")
        self._buffer += data

        if self._uri is None:
            if self._buffer.startswith(delimiter):
                self._buffer.replace(delimiter, "", 1)
            if self._buffer.find(delimiter):
                raw_request, self._buffer = self._buffer.split(delimiter, 1)
                self._add_request(raw_request.decode("utf-8"))
            else:
                return

        if (delimiter + delimiter) not in self._buffer:
            self._no_ending = True
            return

        data_header: bytes
        data_header, self._body = self._buffer.split((delimiter + delimiter), 1)
        self._no_ending = False
        self.add_header(data_header.decode("utf-8"))
        self._buffer = None   


    def _add_request(self, raw_request: str):
        " Getting request values "
        try:
            request_method, request_uri, request_version = raw_request.split(" ", 3)
        except:
            raise RequestError()
        if request_method not in HTTP_METHOD_TOKENS:
            raise NotImplementedError()
        else:
            self._method = request_method
        self._uri = Uri(request_uri)
        if "HTTP" not in request_version:
            raise RequestError()
        else:
            self._version = request_version
        
    def add_header(self, raw_header: str):
        for header_line in raw_header.replace(" ", "").split("\r\n"):
            name, value = header_line.split(":", 1)
            self._header[name] = value

    def append_body(self, data: bytes):
        if not data:
            return
        self._body += data

    def is_complete(self):
        if self._no_ending:
            return False
        

    def method(self):
        return self._method

    def url(self):
        return self._uri.url()

    def resource(self):
        return self._uri.type()

    def resource(self, type:str):
        return self._uri.type() == type

    def body_size(self) -> int:
        return len(self._body)
    
    def read_header(self, name: str) -> str:
        return self._header[name]

    