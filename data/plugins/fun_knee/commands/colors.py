from src.modules.formated_terminal import *


# Must be in every single command files.
def export() -> dict:
    description = "I allow you to check colors display !"
    args = []
    permission = 0 
    
    return { "description" : description, "args" : args, "permission" : permission }


# Must be in every single command files.
def execute(req_args : list[str], opt_args : dict = {}, suplementary : dict = {}) -> None:
    print_color_samples()
    
    