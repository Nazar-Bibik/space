from router import Element
from finder import html

class Stars(Element):
    def path(self) -> str:
        return "stars"

    def children(self) -> list['Element']:
        return

    def html(self) -> str:
        return "stars.html"

    def options(self) -> bool:
        return True