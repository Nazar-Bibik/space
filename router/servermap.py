from router.element import Element
from router.elements.home import Home
from router.elements.contact import Contact
from router.elements.stars import Stars
from finder import html

class ServerMap(Element):
    def __init__(self):
        super().__init__()
        self._server_tree({self.__class__.__name__: self})
        print("Done!")

    def path(self) -> str:
        return ""

    def children(self) -> list:
        return (
            Home,
            Stars,
            Contact,
        )

    def html(self) -> str:
        return html("index.html")

    def options(self) -> bool:
        return True