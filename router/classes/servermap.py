# Copyright (C) 2023  Nazar Bibik

from router.classes.element import Element
from router.elements.home import *
from router.elements.stars import *
from router.elements.contact import *
from router.elements.notfound import *
from finder import index

class ServerMap(Element):
    _reference: dict['Element']
    _not_found: Element

    def __init__(self):
        self._path = ""
        self._html = index()
        self._allow_embeded = False
        self._children = list()
        # self._reference = self._server_tree({self.__class__.__name__: self})
        self._reference = self._server_tree(dict())
        self._not_found = NotFound()
        print("ServerMap complete!")

    def children(self) -> list:
        return (
            Home,
            Stars,
            Contact,
            NotFound,
        )
        
    def serve(self, url: str) -> str | None:
        content: str
        if url == "/":
            return self.serve("home")
        else:
            if not url.startswith("/"):
                url = "/" + url
            if not url.endswith("/"):
                url += "/"
            content = super().serve(url)
        if content is None:
            return None
        # Remove after debugging html
        return index().replace("{servermap}", content)
        # content = self._html.replace("{servermap}", content)
        # return content
