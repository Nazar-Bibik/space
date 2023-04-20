from router import Element


# class Stars(Element):
#     def path(self) -> str:
#         return "stars"

#     def children(self) -> list['Element']:
#         return

#     def html(self) -> str:
#         return "stars.html"

#     def options(self) -> bool:
#         return True
    

def init(get: str = None):
    name = "stars"
    path = "stars"
    is_embeded = False
    html = "stars.html"
    css = {}
    js = {}
    children = {}

    if get == "name":
        return name

    return Element(name, path, is_embeded, html,\
                    None if css == {} else css, None if js == {} else js, None if children == {} else children)