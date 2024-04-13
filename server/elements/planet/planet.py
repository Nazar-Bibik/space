from server import Element


# class Planet(Element):
#     def path(self) -> str:
#         return "planet"

#     def children(self) -> list['Element']:
#         return

#     def html(self) -> str:
#         return "/planet/planet.html"

#     def css(self) -> str:
#         return "[]"

#     def options(self) -> bool:
#         return
    

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