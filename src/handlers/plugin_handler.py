from files import json_edit
from terminal import *

import os


global_settings = json_edit.read("data/settings/global_settings.json")



# Retrives the loading root path of plugins
def pathfetch(exceptions: list[str] = []) -> dict:
    command_pack_directory : str = global_settings["plugins_directory"]
    pathfetch_output : dict = {
            "__list__": [],
            "__prefix__": {},
            "__data__": {}
        }

    if not os.path.exists(command_pack_directory): # Check if the given path in the settings acctually exist
        print_err("CLIF_DEFAULT.PLUGIN_DIR_NOT_FOUND", True)
        return {}
        
    for (dir_path, dir_names, file_names) in os.walk(command_pack_directory):

        if 'data.json' in file_names: # This means that a plugin DATA has been found.
            plugin_data = json_edit.read(dir_path + '/data.json')  
            if plugin_data["name"] in exceptions: continue
            
            pathfetch_output["__data__"][plugin_data["id"]] = plugin_data
            pathfetch_output["__data__"][plugin_data["id"]]["file"] = dir_path

            pathfetch_output["__prefix__"][plugin_data["prefix"]] = dir_path.replace("/", ".") # Useful for command execution with prefix
            pathfetch_output["__list__"].append(dir_path.replace("/", ".")) # Useful for identifying what plugins are registered without iterating through the whole hashmap
        else: continue
        

    return pathfetch_output


def register_plugins(exceptions : list[str] = []) -> None:
    register_path : str = global_settings["plugins_rgstr_directory"]
    pathloads = pathfetch(exceptions)

    json_edit.write(register_path, pathloads)
    print_success("CLIF_DEFAULT.PLUGINS_REGISTERED", placeholders= {"%registered_plugin_count%": str(len(pathloads) - 1)})
    


