# Copyright (C) 2023  Nazar Bibik

import finder
from security.exceptions import InternalError

class Element():
    """ 
    Web elements that make HTML page.
    This class collects everything needed to show html element to client.
    It also states what is requierd from client to recieve this element.
    As well as permissions when requesting this element.
    """
    _name: str
    _path: str
    _is_embeded: bool
    _html: str
    _css: set[str]
    _js: set[str]
    _children: set['Element']


    def __init__(self, name: str, path: str, is_embeded: bool, html: str, css: set[str] = None, js: set[str] = None, children: set['function'] = None):
        self._name = name
        self._path = path
        self._is_embeded = is_embeded
        self._html = html
        self._css = css
        self._js = js
        self._children = children


    def __iter__(cls):
        return iter(cls._name)
    

    def _server_tree(self, reference: dict) -> dict:
        reference[self._name] = self

        children = self._children
        self._children = set()

        if children:
            for child in children:
                if self._name == child("name"):
                    raise InternalError()
                if child("name") in reference:
                    self._children.add(reference[child("name")])
                else:
                    created_child = child()
                    self._children.add(created_child)
                    reference.update(created_child._server_tree(reference))
        return reference
    
    def path(self) -> str:
        return self._path
    
    def name(self) -> str:
        return self._name

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
            page = page.replace("{element " + str(child_element.name()) + "}", child_element.assemble())
        return page
        


"""
A template for element class :


from router import Element

def init(get: str = None):
    name = ""
    path = ""
    is_embeded = True
    html = ""
    css = {}
    js = {}
    children = {}

    if get == "name":
        return name

    return Element(name, path, is_embeded, html,\
                    None if css == {} else css, None if js == {} else js, None if children == {} else children)
"""


