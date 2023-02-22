
class Element():
    """ 
    Web elements that make HTML page.
    This class collects everything needed to show html element to client.
    It also states what is requierd from client to recieve this element.
    As well as permissions when requesting this element.
    """
    _path: str
    _html: str
    _css: str
    _js: str
    _media: str
    _allow-embeded: bool
    _children: list
