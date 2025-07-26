import os


def make_file(name : str, content : list[str] = ["# File created"]):
    with open(name, "w") as file: file.write("\n".join(content))
