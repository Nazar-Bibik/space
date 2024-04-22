from server import Element


def init(get: str = None):
    name = "contact"
    path = "contact"
    is_embeded = False
    html = "contact.html"
    css = {}
    js = {}
    children = {}

    if get == "name":
        return name

    return Element(name, path, is_embeded, html,\
                    None if css == {} else css, None if js == {} else js, None if children == {} else children)