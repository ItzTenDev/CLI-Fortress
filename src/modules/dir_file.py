import os


def make_dir(name : str):
    os.mkdir(name)


def make_file(name : str, content : list[str] = ["# File created"]):
    with open(name, "w") as file:
        file.write("\n".join(content))