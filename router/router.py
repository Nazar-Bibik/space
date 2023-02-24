from router import Request, Response, ServerMap
from finder import file


IMPLEMENTED_HTTP_METHODS = ["OPTIONS", "GET", "PUT", "POST", "HEAD"]


def serve(request: Request, servermap: ServerMap) -> bytes:
    response: Response

    if request.method() == "GET":

        if request.resource("LINK") or request.resource("HOME"):
            content = servermap.serve(request.url())
            if not content:
                response = Response("404", "Not Found", "HTTP/1.0")
                content = servermap.serve_404()
            else:
                response = Response("200", "OK", "HTTP/1.0")
            response.append_body(bytes(content, "utf-8"))   
        
        if request.resource("FILE"):
            response = Response("200", "OK", "HTTP/1.0")
            content = file(request.url())
            response.append_body(content) 

    return response.serve() 

# def response_options():
