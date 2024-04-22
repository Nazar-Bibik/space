from server import Element
from finder import html
import server.elements.planet.planet as planet
    

def init(get: str = None):
    name = "home"
    path = "home"
    is_embeded = False
    html = "home.html"
    css = {}
    js = {}
    children = {planet.init}

    if get == "name":
        return name

    return Element(name, path, is_embeded, html,\
                    None if css == {} else css, None if js == {} else js, None if children == {} else children)