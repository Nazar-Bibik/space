from security.exceptions import RequestNotFound
from security.exceptions import RequestError
from urllib import parse


class Uri():
    """ This is uri class """
    _url: str
    _querry: dict
    _type: str
    TYPES = ["HOME", "LINK", "API", "FILE"]

    def __init__(self, uri_stream: str):
        raw_querry = None
        if "?" not in uri_stream:
            self._url = uri_stream
        else:
            self._url, raw_querry = uri_stream.split("?", 1)

        if "/" == self._url:
            self._type = "HOME"
        elif self._url.startswith("/api/"):
            self._type = "API"
        elif self._url.startswith("/file/"):
            self._type = "FILE"
        else:
            self._type = "LINK"

        self._querry = None
        if raw_querry:
            self._querry = dict()
            try:
                for querry_variable in raw_querry.split("&"):
                    var_name, var_val = querry_variable.split("=", 1)
                    var_val = parse.unquote(var_val.replace("+", " "), encoding='utf-8')
                    self._querry[var_name] = var_val
            except ValueError:
                raise RequestNotFound
            except:
                raise

    def print_info(self):
        print(self._type)
        print(self._url)
        print(self._querry)

    def type(self):
        return self._type
