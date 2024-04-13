from server import Element


class Contact(Element):
    def path(self) -> str:
        return "contact"

    def children(self) -> list['Element']:
        return

    def html(self) -> str:
        return "contact.html"

    def options(self) -> bool:
        return
    

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