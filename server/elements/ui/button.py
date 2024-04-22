from server import Element

class Button(Element):
    def path(self) -> str:
        return "ui_button"

    def children(self) -> list['Element']:
        return

    def html(self) -> str:
        return

    def options(self) -> bool:
        return