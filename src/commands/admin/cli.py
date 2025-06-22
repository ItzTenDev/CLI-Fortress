from math import *
from modules.colored_terminal import *

import modules.json_edit as json

# Must be in every single command files.
def export() -> dict:
    name = "cos"
    description = "I allow you change properties of the CLI"
    args = ["sub-command", "args..."]
    usage = name + "".join([" <" + arg + ">" for arg in args])
    permission = 0 
    
    return { "name" : name, "description" : description, "args" : args, "usage" : usage, "permission" : permission }


# Must be in every single command files.
def execute(user, args, database) -> None:
    if (args[0] == "rename") and args[1]:
        previous_name = str(json.read("register/session.json")["sys_name"])
        
        json.set_property("register/session.json", {"sys_name": " ".join(args[1:])})
        printf("§6> §f§l" + previous_name + "§r has successfully been rename to : §e" + " ".join(args[1:]) +" §r!\n", False)
    
    