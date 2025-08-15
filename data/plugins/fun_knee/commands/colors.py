from terminal import *


# Must be in every single command files.
def export() -> dict:
    description = "I allow you to check colors display !"
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
    print_color_samples()
    
    