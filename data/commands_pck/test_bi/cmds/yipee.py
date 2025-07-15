from math import *
from modules.formated_terminal import *


# Must be in every single command files.
def export() -> dict:
    name = "yipee"
    description = "Be proud of yourself !"
    args = ["hapiness level"]
    usage = name + "".join([" <" + arg + ">" for arg in args])
    permission = 0 
    
    return { "name" : name, "description" : description, "args" : args, "usage" : usage, "permission" : permission }


# Must be in every single command files.
def execute(user, args, database) -> None:
    printf("🎉🎊 §6 yipe" + "e"*int(args[0]))
    
    