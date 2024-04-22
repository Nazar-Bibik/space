# Copyright (C) 2023  Nazar Bibik

from server import Request, Response, ServerMap
from finder import file
from security import exceptions


IMPLEMENTED_HTTP_METHODS = ["OPTIONS", "GET", "PUT", "POST", "HEAD"]


# def resource_info(response: Response, servermap: ServerMap):
#     if request.resource("LINK"):
#         return 

def _serve_error(err: Exception, method: str) -> Response:
    if err == TimeoutError:
        return _serve_error(exceptions.ConnectionTimeOut, method)
    
    if err in exceptions.HTTP_EXCEPTION_ARRAY:
        return Response(err.http_code, err.http_message, method)
    
    return _serve_error(exceptions.InternalError, method)


def _serve_file(request: Request) -> Response:
    try:
        content = file(request.url())
    except FileNotFoundError:
        return _serve_error(exceptions.RequestNotFound, request.version())
    except OSError:
        print(OSError)
        return _serve_error(exceptions.InternalError, request.version())
    response = Response("200", "OK", "HTTP/1.1")
    response.append_body(content) 
    response.add_header("Connection", "keep-alive")
    return response


def _serve_link(request: Request, servermap: ServerMap, charset: str) -> Response:
    response: Response
    content = servermap.serve(request.url())
    if content is None:
        response = _serve_error(exceptions.RequestNotFound, request.version())
        response.append_body(bytes(servermap.serve("/404/"), charset))
    else:
        response = Response("200", "OK", "HTTP/1.1")
        response.append_body(bytes(content, charset)) 
    response.add_header("Connection", "keep-alive")
    return response


def serve(request: Request, servermap: ServerMap, err: Exception = None) -> bytes:
    response: Response
    charset = n if (n:= request.read_header("charset")) else "utf-8"

    if err != None:
        response = _serve_error(err, request.version())
        if err == exceptions.RequestNotFound:
            response.append_body(bytes(servermap.serve("/404/"), charset))
        response.add_header("Connection", "close")
        return response.serve()

    if request.method() == "GET":

        if request.resource("LINK"):
            return _serve_link(request, servermap, charset).serve()
        
        if request.resource("FILE"):
            return _serve_file(request).serve()

    return _serve_error(exceptions.NotImplementedError, request.method()).serve() 



# def response_options():
