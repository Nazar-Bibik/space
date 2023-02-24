from router import Element
from finder import html

class Contact(Element):
    def path(self) -> str:
        return "contact"

    def children(self) -> list['Element']:
        return

    def html(self) -> str:
        return html("contact.html")

    def options(self) -> bool:
        return