from terminal import *


# Must be in every single command files.
def export() -> dict:
    description = "Executes the cls command in command prompt."
    args = ["r:pancakes"]
    sub_commands = {
        "new": {
            "description": "Create a new plugin template",
            "args": ["o:--name", "o:--description"],
            "permission": 0,
            "pathload_name": "$plugin new"
        },
        "delete": {
            "description": "Deletes an existing plugin permanently",
            "args": ["r:name"],
            "permission": 0,
            "pathload_name": "$plugin delete"
        },
        "help": {
            "description": "Check informations about a plugin's command",
            "args": ["r:plugin", "o:--command", "o:--c"],
            "permission": 0,
            "pathload_name": "$plugin help"
        },
    }
    permission = 0
    
    return { 
        "description" : description, 
        "args" : args, 
        "sub_commands": sub_commands,
        "permission" : permission 
        }


# Must be in every single command files.
def execute(req_args : list[str], opt_args : dict = {}, suplementary : dict = {}) -> None:
    pancakes : int = int(req_args[0])
    print(f"There is {pancakes} pancakes for You !")
    