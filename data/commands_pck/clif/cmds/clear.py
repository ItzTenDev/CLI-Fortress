from math import *
from modules.formated_terminal import *

import modules.terminal as terminal

# Must be in every single command files.
def export() -> dict:
    name = "clear"
    description = "Executes the cls command in command prompt."
    args = []
    usage = name + "".join([" <" + arg + ">" for arg in args])
    permission = 0 
    
    return { "name" : name, "description" : description, "args" : args, "usage" : usage, "permission" : permission }


# Must be in every single command files.
def execute(user, args, database) -> None:
    terminal.run_command("cls")
    
    
    