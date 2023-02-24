from router import Element
from finder import html

class Home(Element):
    def path(self) -> str:
        return "home"

    def children(self) -> list['Element']:
        return

    def html(self) -> str:
        return html("home.html")

    def options(self) -> bool:
        return True