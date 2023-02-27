import os

def file(path: str) -> str:
    if path.startswith("/"):
        path = path.replace("/", "", 1)
    with open("finder/" + path, "rb") as file:
        return file.read()

def html(path: str) -> str:
    with open("finder/html/" + path, "r") as file:
        return file.read()

def index() -> str: 
    path = os.getcwd()
    with open(path + "/index.html", "r") as file:
        return file.read()

