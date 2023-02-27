from router import Element
from finder import html

class NotFound(Element):
    def path(self) -> str:
        return "404"

    def children(self) -> list['Element']:
        return

    def html(self) -> str:
        return "404.html"

    def options(self) -> bool:
        return True