

HTTP_RESPONSE_TOKENS = ["a lot..."]

class Response:
    """ This is HTTP response class """
    _code: str
    _message: str
    _version: str
    _header: dict
    _body: bytes

    def __init__(self, code: str, message: str, version: str):
        self._code = code
        self._message = message
        self._version = version
        self._header = dict()
        self._body = None



    def add_header(self, header_name, header_value):
        self._header[header_name] = header_value

    
    def print_info(self):
        print(self._code)
        print(self._message)
        print(self._version)
        print(self._header)


    def append_body(self, data: bytes):
        if not self._body:
            self._body = data
        else:
            self._body += data

    def serve(self) -> bytes:
        response = bytes("", "utf-8")
        delimiter = bytes("\r\n", "utf-8")
        status_line = self._version + " " + self._code + " " + self._message
        response += bytes(status_line, "utf-8")
        response += delimiter

        for key, value in self._header.items():
            response += bytes(key + " : " + value, "utf-8")
            response += delimiter

        response += delimiter

        if self._body:
            response += self._body

        return response




    