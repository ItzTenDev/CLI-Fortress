from terminal import *


# Must be in every single command files.
def export() -> dict:
    description = "I return pong as fast as possible !"
    args = ["r:message"]
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

    message = req_args[0]

    def pong(string: str):
        print(string)

    pong(message)