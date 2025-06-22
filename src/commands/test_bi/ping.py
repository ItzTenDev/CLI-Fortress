from math import *
from modules.colored_terminal import *


# Must be in every single command files.
def export() -> dict:
    name = "ping"
    description = "I return pong as fast as possible !"
    args = ["message"]
    usage = name + "".join([" <" + arg + ">" for arg in args])
    permission = 0 

    return { "name" : name, "description" : description, "args" : args, "usage" : usage, "permission" : permission }


# Must be in every single command files.
def execute(user, args, database) -> None:

    message = " ".join(args[0:])

    def pong(string: str):
        print(string)

    pong(message)