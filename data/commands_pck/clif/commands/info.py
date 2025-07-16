from src.modules.formated_terminal import *
from src.modules.cli_reader import *

import src.modules.json_edit as json

# Must be in every single command files.
def export() -> dict:
    name = "info"
    description = "I return pong as fast as possible !"
    args = []
    usage = name + "".join([" <" + arg + ">" for arg in args])
    permission = 0 
    
    return { "name" : name, "description" : description, "args" : args, "usage" : usage, "permission" : permission }


# Must be in every single command files.
def execute(user, args, database) -> None:
    session_data = json.read("data/register/session.json")
    
    display_cli("informations", {
        "%slot_1_k%": "System             ", "%slot_1_v%": session_data["sys_name"],
        "%slot_2_k%": "Loaded Commands    ", "%slot_2_v%": session_data["l_cmds"],
        "%slot_3_k%": "Registered Commands", "%slot_3_v%": session_data["r_cmds"],
        "%slot_4_k%": "                   ", "%slot_4_v%": " ",
        "%slot_5_k%": "                   ", "%slot_5_v%": " ",
        "%slot_6_k%": "                   ", "%slot_6_v%": " ",
        "%slot_7_k%": "                   ", "%slot_7_v%": " ",
        "%slot_8_k%": "                   ", "%slot_8_v%": " "
        })
    
    