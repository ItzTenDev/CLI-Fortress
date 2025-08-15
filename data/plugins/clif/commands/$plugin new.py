from terminal import *

from files import json_edit

import os


settings = json_edit.read("data/settings.json")

# Must be in every single command files.
def export() -> dict:
    parent = "plugin"

    return {"parent": parent}


# Must be in every single command files.
def execute(req_args : list[str], opt_args : dict = {}, suplementary : dict = {}) -> None:
    plugin_name : str = opt_args.get("--name") or "New Plugin"
    description : str = opt_args.get("--description") or "Default description"

    formated_name : str = plugin_name.lower().replace(" ", "_")
    plugin_directory_path : str = settings["plugins_directory"] + (formated_name)
    prefix = formated_name.replace("_", "-")

    try:
        os.mkdir(plugin_directory_path)
        os.mkdir(plugin_directory_path + "/commands/")
        os.mkdir(plugin_directory_path + "/events/")
    except FileExistsError:
        print_err("CLIF.COMMAND.PLUGIN$NEW.PLUGIN_ALREADY_EXIST", placeholders={"%plugin_name%": plugin_name})
        return

    default_data: dict = {
        "name": plugin_name,
        "prefix": prefix,
        "description": description,
        "author": ["Whatever"],
        "version": "1.0.0",
        "id": formated_name.replace("-", "_")
        }

    json_edit.write(plugin_directory_path + "/data.json", default_data)
    
    printf(f"§2█ §fYour plugin §a§n{plugin_name} §r§fhas successfully been created !\n§r§2█ §fIt runs its commands with the prefix: §a{prefix} §8[command] <sub_command/arguments>")
    
    
    