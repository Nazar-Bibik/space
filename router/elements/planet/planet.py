from router import Element
from finder import html

class Planet(Element):
    def path(self) -> str:
        return "planet"

    def children(self) -> list['Element']:
        return

    def html(self) -> str:
        return "/planet/planet.html"

    def css(self) -> str:
        return "[]"

    def options(self) -> bool:
        return