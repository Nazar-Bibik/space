from security.exceptions import RequestNotFound


class Uri()
    _url: str
    _querry: dict
    _type: str
    TYPE: ["HOME", "LINK", "API", "FILE"]

    def __init__(self, uri_stream: str):
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
            for querry_variable
