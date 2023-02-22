from element import Element
from router.elements import *
from typing import Type

class ServerMap(Element):
    def __

    @staticmethod
    def _server_tree(self, node: Type[Element]) -> list:
        branch = list(self)
        for child in self.children():
            branch.append(child._server_tree)


