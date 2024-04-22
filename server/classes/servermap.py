# Copyright (C) 2023  Nazar Bibik

from server.classes.element import Element
import server.elements.home as home
import server.elements.stars as stars
import server.elements.contact as contact
import server.elements.notfound as notfound
import finder

class ServerMap(Element):
    '''
        A root of a server, connected in a tree structure to all the pages.
        Takes url, searches for pages and their embeded children, and returns full html page.
        The root is set to a home page.
    '''


    _reference: dict['Element']

    def __init__(self):
        self._path = ""
        self._html = finder.index()
        self._is_embeded = False
        self._children = self._children()
        self._reference = self._server_tree()
        print("ServerMap complete!")

    def _children(self) -> set:
        return (
            home.init,
            stars.init,
            contact.init,
            notfound.init,
        )
    
    def _server_tree(self) -> dict:
        reference = dict()

        children = self._children
        self._children = set()

        for child in children:
            created_child = child()
            self._children.add(created_child)
            reference.update(created_child._server_tree(reference))
        return reference
        
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

        return self._html.replace("{servermap}", content)

