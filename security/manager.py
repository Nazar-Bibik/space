
import os
from router import Request

class Manager():
    """
        A connection management class, that stands between socket (TCP/IP) and HTTP
    """

    _host: str
    _client: tuple[str, int]
    _keep_alive: bool
    _socket_buffer_size: int
    _request_size: int
    _batch_size: int
    _retry: int

    def __init__(self, client_address: tuple):
        self._host = os.environ["SPACE_IP"] + ":" + os.environ["SPACE_PORT"]
        self._client = client_address
        self._keep_alive = True
        self._socket_buffer_size = int(os.environ["SOCKET_BUFFER"])
        self._request_size = 0
        self._retry = int(os.environ["RETRY_INT"])

    def ping_response(self) -> bytes:
        "When there is a ping to server. A response is server's ip address."
        self.kill()
        return self._host.encode("ascii")
    
    def keep_alive(self) -> bool:
        return self._keep_alive
    
    def kill(self):
        self._keep_alive = False

    def buffer_size(self) -> int:
        return self._socket_buffer_size
    
    def uncomplete_request(self, request: Request) -> bool:
        if self.request_expect_header(request):
            return True
        if self.request_expect_body(request):
            return True
        return False
    
    def request_expect_body(self, request: Request) -> bool:
        if request.method() in ("PUT", "PATH", "DELETE", "POST"):
            if int(request.read_header("Content-Length")) != request.body_size():
                return True
        return False
        
    def request_expect_header(self, request: Request) -> bool:
        if request._no_ending and (self._batch_size == self._socket_buffer_size):
            return True
        return False

    def batch_size(self) -> int:
        return self._batch_size
    
    def batch_size(self, data: bytes):
        self._batch_size = len(data)

