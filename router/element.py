
class Element():
    """ 
    Web elements that make HTML page.
    This class collects everything needed to show html element to client.
    It also states what is requierd from client to recieve this element.
    As well as permissions when requesting this element.
    """
    _path: str
    _html: list
    _css: str
    _js: str
    _media: str
    _allow-embeded: bool
    _children: list

    def __init__(self, reference: list):
        self._path = path()
        self._children = None
        for child in reference:
            if child in children():
                self._children.append(child)
        self._html = html()
        self._allow-embeded = options()

    @staticmethod
    def path() -> str:
        return

    @staticmethod
    def children() -> list:
        return

    @staticmethod
    def html() -> str:
        return

    @staticmethod
    def options() -> bool:
        return
