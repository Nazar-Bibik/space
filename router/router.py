
from router import Request, Response, ServerMap






def serve(request: Request, servermap: ServerMap):
    if request.method() == "GET":
        return None
    pass