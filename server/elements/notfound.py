from server import Element


# class NotFound(Element):
#     def path(self) -> str:
#         return "404"

#     def children(self) -> list['Element']:
#         return

#     def html(self) -> str:
#         return "404.html"

#     def options(self) -> bool:
#         return True


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