from math import *
from modules.colored_terminal import *
from modules.cli_reader import *
from datetime import *

import modules.json_edit as json

# Must be in every single command files.
def export() -> dict:
    name = "help"
    description = "allow you to see infos about commands"
    args = ["command"]
    usage = name + "".join([" <" + arg + ">" for arg in args])
    permission = 0 
    
    return { "name" : name, "description" : description, "args" : args, "usage" : usage, "permission" : permission }


# Must be in every single command files.
def execute(user, args, database) -> None:
    argument = args[0]
    command_data = json.read("data/register/commands.json")
    
    
    if argument == "all":
        category_list = []
        
        for i in command_data:
            data = command_data[i]
            if data["category"] not in category_list: category_list.append(data["category"])
            
        for category in category_list:
            printf("\n§f -- §6 " + category.replace("_", " ") + " §f ---------------")
            cmds = list(filter(lambda cmd: command_data[cmd]["category"]== category, command_data))
            printf(", ".join(cmds))
            
    elif argument in command_data:
            display_cli("help_embed", {
        "%icon%": "🎓",
        "%title%": command_data[argument]["name"],
        "%description%": command_data[argument]["description"],
        "%usage%": command_data[argument]["usage"],
        "%category%": command_data[argument]["category"].replace("_", " "),
        "%color%": "§6",
        "%footer%": str(datetime.now().strftime("%m/%d/%Y - %H:%M:%S")),

        })
    else:
        printf("§c# §f" + argument + " §rhas not been found.", False)
    