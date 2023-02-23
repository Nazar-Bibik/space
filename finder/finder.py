import os

def html(path: str) -> str:
    with open("finder/" + path, "r") as file:
        return file.read()
