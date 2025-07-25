from src.modules.formated_terminal import *

import src.modules.dir_file as df
import src.modules.json_edit as json_edit
import src.modules.terminal as terminal


global_settings = json_edit.read("data/settings/global_settings.json")

# Must be in every single command files.
def export() -> dict:
    parent = "plugin"

    return {"parent": parent}


# Must be in every single command files.
def execute(req_args : list[str], opt_args : dict = {}, suplementary : dict = {}) -> None:    
    printf(f"§6▓ §fThis command is under construction")
    
    
    