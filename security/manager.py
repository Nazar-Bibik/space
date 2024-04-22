# Copyright (C) 2023  Nazar Bibik

import os
import socket
from server.classes.request import Request
from security.exceptions import RequestError

class Manager():
    """
        A connection management class, that stands between socket (TCP/IP) and HTTP
    """

    _host: str
    _client: tuple[str, int]
    _keep_alive: bool
    _socket_buffer_size: int
    _request_size: int
    _retry: int
    _error: Exception

    def __init__(self, client_address: tuple):
        self._host = os.environ["SPACE_IP"] + ":" + os.environ["SPACE_PORT"]
        self._client = client_address
        self._keep_alive = True
        self._socket_buffer_size = int(os.environ["SOCKET_BUFFER"])
        self._request_size = 0
        self._retry = int(os.environ["RETRY_INT"])
        self._error = None
    
    def keep_alive(self) -> bool:
        return self._keep_alive
    
    def kill(self):
        self._keep_alive = False

    def buffer_size(self) -> int:
        return self._socket_buffer_size
    
    # Check if a header or body is incomplete
    def uncomplete_request(self, request: Request) -> bool:
        if self.request_expect_header(request):
            return True
        if self.request_expect_body(request):
            if self._retry == 0:
                raise TimeoutError
            return True
        return False
    
    def request_expect_body(self, request: Request) -> bool:
        if request.method() in ("PUT", "PATH", "DELETE", "POST"):
            content_length = request.read_header("Content-Length")
            if content_length is None:
                return False
            if int(content_length) < request.body_size():
                return True
            if int(content_length) > request.body_size():
                self.kill()
                raise RequestError
        return False
        
    def request_expect_header(self, request: Request) -> bool:
        return not request.is_complete()

    def dropped_data(self):
        if self._retry <= 0:
            self.kill()
            return
        self._retry -= 1

    def flush(self, connection: socket.socket, data):
        if self._error == TimeoutError:
            return
        while True:
            if data is None:
                return
            try:
                data = connection.recv(self._socket_buffer_size)
            except TimeoutError:
                return
    
    def catch(self, err: 'Exception'):
        self._error = err
        self.kill()

    def exception(self) -> Exception:
        return self._error
    
    def verify_request(self, request: Request):
        keep_alive = request.read_header("connection")
        if keep_alive == None:
            self.kill()
        else:
            if keep_alive.lower() != "keep-alive":
                self.kill()
        self._error = None
        return