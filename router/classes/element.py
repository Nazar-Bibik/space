# Copyright (C) 2023  Nazar Bibik

import finder

class Element():
    """ 
    Web elements that make HTML page.
    This class collects everything needed to show html element to client.
    It also states what is requierd from client to recieve this element.
    As well as permissions when requesting this element.
    """
    _name: str
    _path: str
    _html: str
    _css: str
    _js: str
    _media: str
    _allow_embeded: bool
    _children: list['Element']

    def path(self) -> str:
        return

    def children(self) -> list['Element']:
        return

    def html(self) -> str:
        return

    def options(self) -> bool:
        return

    def __init__(self):
        self._path = self.path()
        self._children = list()
        self._html = self.html()
        self._allow_embeded = self.options()

    def __iter__(cls):
        return iter(cls.__name__)

    def _server_tree(self, reference: dict) -> dict:
        reference[self.__class__.__name__] = self

        self._children = list()

        if self.children():
            for child in self.children():
                if child.__name__ in reference:
                    self._children.append(reference[child.__name__])
                else:
                    created_child = child()
                    self._children.append(created_child)
                    reference.update(created_child._server_tree(reference))
        return reference

    def serve(self, url: str) -> str | None:
        if not url:
            return None
        if url == self._path or url == (self._path + "/"):
            return self.assemble()
        url = url.replace(self._path + "/", "", 1)
        for child in self._children:
            if url.startswith(child.path() + "/"):
                return child.serve(url)
        return None


    def assemble(self, data: dict = None) -> str:
        page = finder.html(self._html)
        if data:
            for name, value in data.items():
                page = page.replace("{data " + str(name) + "}", value)
        for child_element in self._children:
            page = page.replace("{element " + str(child_element.__class__.__name__) + "}", child_element.assemble())
        return page
        


"""
A template for element class inherit:


from router import Element
from finder import html

class NAME(Element):
    def path(self) -> str:
        return

    def children(self) -> list['Element']:
        return

    def html(self) -> str:
        return

    def css(self) -> str:
        return "[]"

    def options(self) -> bool:
        return
"""