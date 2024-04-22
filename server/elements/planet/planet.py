from server import Element
   

def init(get: str = None):
    name = "planet"
    path = "planet"
    is_embeded = True
    html = "/planet/planet.html"
    css = {}
    js = {}
    children = {}

    if get == "name":
        return name

    return Element(name, path, is_embeded, html,\
                    None if css == {} else css, None if js == {} else js, None if children == {} else children)