from src.modules.formated_terminal import *

import src.modules.json_edit as json_edit
import src.modules.terminal as terminal

import os


global_settings = json_edit.read("data/settings/global_settings.json")



# Retrives the loading root path of plugins
def pathfetch(exceptions: list[str] = []) -> dict:
    command_pack_directory : str = global_settings["plugins_directory"]
    pathfetch_output : dict = {
            "__list__": [],
        }

    if not os.path.exists(command_pack_directory): # Check if the given path in the settings acctually exist
        terminal.print_err("CLIF_DEFAULT.PLUGIN_DIR_NOT_FOUND", True)
        return {}
        
    for (dir_path, dir_names, file_names) in os.walk(command_pack_directory):

        if 'data.json' in file_names: # This means that a plugin DATA has been found.
            plugin_data = json_edit.read(dir_path + '/data.json')  
            if plugin_data["name"] in exceptions: continue

            pathfetch_output[plugin_data["prefix"]] = dir_path.replace("/", ".") # Useful for command execution with prefix
            pathfetch_output["__list__"].append(dir_path.replace("/", ".")) # Useful for identifying what plugins are registered without iterating through the whole hashmap
        else: continue
        

    return pathfetch_output


def register_plugins(exceptions : list[str] = []) -> None:
    register_path : str = global_settings["plugins_rgstr_directory"]
    pathloads = pathfetch(exceptions)

    json_edit.write(register_path, pathloads)
    terminal.print_success("CLIF_DEFAULT.PLUGINS_REGISTERED", placeholders= {"%registered_plugin_count%": str(len(pathloads) - 1)})
    


