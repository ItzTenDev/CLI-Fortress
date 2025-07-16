from math import *
from src.modules.formated_terminal import *


# Must be in every single command files.
def export() -> dict:
    name = "hello"
    description = "I say hello !"
    args = []
    usage = name + "".join([" <" + arg + ">" for arg in args])
    permission = 0 

    return { "name" : name, "description" : description, "args" : args, "usage" : usage, "permission" : permission }


# Must be in every single command files.
def execute(user, args, database) -> None:
    print("hi")