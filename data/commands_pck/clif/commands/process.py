from src.modules.formated_terminal import *

import os
import src.modules.terminal as terminal


# Must be in every single command files.
def export() -> dict:
    name = "process"
    description = "I get acess to every control of the current process of the CLI !"
    args = ["sub_command"]
    usage = name + "".join([" <" + arg + ">" for arg in args])
    permission = 0

    return { "name" : name, "description" : description, "args" : args, "usage" : usage, "permission" : permission }


# Must be in every single command files.
def execute(user, args, database) -> None:

    print(args)

    if args[0] == "quit": quit()