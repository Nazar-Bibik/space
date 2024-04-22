from server import Element


def init(get: str = None):
    name = "notfound"
    path = "404"
    is_embeded = False
    html = "404.html"
    css = {}
    js = {}
    children = {}

    if get == "name":
        return name

    return Element(name, path, is_embeded, html,\
                    None if css == {} else css, None if js == {} else js, None if children == {} else children)