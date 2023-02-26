# Copyright (C) 2023  Nazar Bibik

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


    def add_data(self, data: bytes):
        if not data:
            return
        if not self._no_ending:
            self.append_body(data)
            return
        
        delimiter = bytes("\r\n", "utf-8")
        self._buffer += data
          
        if (delimiter + delimiter) in self._buffer:
            self._buffer, self._body = self._buffer.split((delimiter + delimiter), 1)
            try:
                self._add_request()
            except RequestError:
                raise
            self._no_ending = False
            

    def _add_request(self):
        delimiter = bytes("\r\n", "utf-8")
        try:
            if self._buffer.startswith(delimiter):
                self._buffer.replace(delimiter, "", 1)

            raw_start_line, raw_header = self._buffer.split(delimiter, 1)
            self._add_start_line(raw_start_line.decode("utf-8"))
            self._add_header(raw_header.decode("utf-8"))
            self._buffer = None   
        except:
            raise RequestError

    def _add_start_line(self, raw_request: str):
        " Getting request values "
        try:
            request_method, request_uri, request_version = raw_request.split(" ", 3)
        except:
            raise RequestError
        if request_method not in HTTP_METHOD_TOKENS:
            raise NotImplementedError
        else:
            self._method = request_method
        self._uri = Uri(request_uri)
        if "HTTP" not in request_version:
            raise RequestError
        else:
            self._version = request_version
        
    def _add_header(self, raw_header: str):
        try:
            for header_line in raw_header.replace(" ", "").split("\r\n"):
                name, value = header_line.split(":", 1)
                self._header[name.lower()] = value
        except:
            raise RequestError

    def assemble(self):
        if not self._no_ending:
            return
        if self._buffer.endswith(bytes("\r\n", "utf-8")):
            self._add_request()
        raise RequestError

    def append_body(self, data: bytes):
        if not data:
            return
        self._body += data

    def is_complete(self):
        if self._no_ending:
            return False
        return True

    def method(self) -> str:
        return self._method

    def url(self):
        return self._uri.url()

    def resource(self):
        return self._uri.type()

    def resource(self, type:str):
        return self._uri.type() == type

    def body_size(self) -> int:
        return len(self._body)
    
    def read_header(self, name: str) -> str | None:
        try:
            return self._header[name]
        except:
            return None

    def version(self) -> str:
        return self._version if self._version else "HTTP/1.1"
    