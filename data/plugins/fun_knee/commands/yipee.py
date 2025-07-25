from src.modules.formated_terminal import *


# Must be in every single command files.
def export() -> dict:
    description = "Be proud of yourself !"
    args = ["r:hapiness level"]
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
    printf("🎉🎊 §6 yipe" + "e"*int(req_args[0]))
    
    