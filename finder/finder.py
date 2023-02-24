import os

def file(path: str) -> str:
    if not path.startswith(("file/", "/file/")):
        path += "file/"
    with open("finder/" + path, "rb") as file:
        return file.read()

def html(path: str) -> str:
    with open("finder/html/" + path, "r") as file:
        return file.read()

def index() -> str: 
    path = os.getcwd()
    with open(path + "/index.html", "r") as file:
        return file.read()

