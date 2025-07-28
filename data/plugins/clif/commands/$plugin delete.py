from src.modules.formated_terminal import *

import src.modules.dir_file as df
import src.modules.json_edit as json_edit
import src.modules.terminal as terminal

import os
import shutil

global_settings = json_edit.read("data/settings/global_settings.json")

# Must be in every single command files.
def export() -> dict:
    parent = "plugin"

    return {"parent": parent}


# Must be in every single command files.
def execute(req_args : list[str], opt_args : dict = {}, suplementary : dict = {}) -> None:    
    plugin_name = req_args[0]
    essential_plugin_list = ["clif"]

    formated_name : str = plugin_name.lower().replace(" ", "_")
    plugin_directory_path : str = global_settings["plugins_directory"] + (formated_name)

    if not os.path.exists(plugin_directory_path):
        terminal.print_err("CLIF.COMMAND.PLUGIN$DELETE.PLUGIN_PATH_NOT_FOUND", placeholders={"%pack_path%": plugin_directory_path})
        return
    
    if plugin_name in essential_plugin_list:
        return
    
    try:
        shutil.rmtree(plugin_directory_path)
    except OSError as e:
        printf(f"Error deleting directory: {e}")
        return
    
    printf(f"§2▓ §fThe plugin §a§n{plugin_name} §r§fhas successfully been deleted from CLIF !")