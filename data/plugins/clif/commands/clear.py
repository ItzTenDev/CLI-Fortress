from terminal import *


# Must be in every single command files.
def export() -> dict:
    description = "Executes the cls command in command prompt."
    args = []
    sub_commands = {}
    permission = 0
    
    return { 
        "description" : description, 
        "args" : args, 
        "sub_commands": sub_commands,
        "permission" : permission 
        }



# Must be in every single command files.
def execute(req_args : list[str], opt_args : dict = {}, suplementary : dict = {}) -> None:
    run_command("cls")
    
    
    