from src.modules.formated_terminal import *

import src.modules.terminal as terminal

# Must be in every single command files.
def export() -> dict:
    description = "Executes the cls command in command prompt."
    args = []
    permission = 0 
    
    return { "description" : description, "args" : args, "permission" : permission }


# Must be in every single command files.
def execute(req_args : list[str], opt_args : dict = {}, suplementary : dict = {}) -> None:
    terminal.run_command("cls")
    
    
    