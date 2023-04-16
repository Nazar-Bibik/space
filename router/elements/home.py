from router import Element
from finder import html
from router.elements.planet.planet import Planet

class Home(Element):
    def path(self) -> str:
        return "home"

    def children(self) -> list['Element']:
        return [Planet]

    def html(self) -> str:
        return "home.html"

    def options(self) -> bool:
        return True