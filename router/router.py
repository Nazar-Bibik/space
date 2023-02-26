# Copyright (C) 2023  Nazar Bibik

from router import Request, Response, ServerMap
from finder import file
from security import exceptions


IMPLEMENTED_HTTP_METHODS = ["OPTIONS", "GET", "PUT", "POST", "HEAD"]


# def resource_info(response: Response, servermap: ServerMap):
#     if request.resource("LINK"):
#         return 

def _serve_error(err: Exception, method: str) -> Response:
    if err == TimeoutError:
        return Response(exceptions.ConnectionTimeOut.http_code, exceptions.ConnectionTimeOut.http_message, method)
    
    if err in exceptions.HTTP_EXCEPTION_ARRAY:
        return Response(err.http_code, err.http_message, method)
    
    return _serve_error(exceptions.InternalError, method)

def serve(request: Request, servermap: ServerMap, err: Exception) -> bytes:
    response: Response
    charset = n if (n:= request.read_header("charset")) else "utf-8"

    if err != None:
        response = _serve_error(err, request.version())
        if err == exceptions.RequestNotFound:
            response.append_body(bytes(servermap.serve("/404/"), charset))
        return response.serve()

    if request.method() == "GET":

        if request.resource("LINK") or request.resource("HOME"):
            content = servermap.serve(request.url())
            if not content:
                return serve(request, servermap, exceptions.RequestNotFound)
            else:
                response = Response("200", "OK", "HTTP/1.0")
            response.append_body(bytes(content, charset))   
        
        if request.resource("FILE"):
            response = Response("200", "OK", "HTTP/1.0")
            content = file(request.url())
            response.append_body(content) 

    return response.serve() 



# def response_options():
