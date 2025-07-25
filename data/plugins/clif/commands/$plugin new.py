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
    name : str = opt_args.get("--name") or "New Plugin"
    description : str = opt_args.get("--description") or "Default description"

    formated_name : str = name.lower().replace(" ", "_")
    plugin_directory_path : str = global_settings["plugins_directory"] + (formated_name)
    prefix = formated_name.replace("_", "-")

    try:
        df.make_dir(plugin_directory_path)
        df.make_dir(plugin_directory_path + "/commands/")
        df.make_dir(plugin_directory_path + "/events/")
    except FileExistsError:
        terminal.print_err("CLIF.COMMAND.PLUGIN$NEW.PLUGIN_ALREADY_EXIST", placeholders={"%plugin_name%": name})
        return

    default_data: dict = {
        "name": name,
        "prefix": prefix,
        "description": description,
        "author": "Whatever"
        }

    json_edit.write(plugin_directory_path + "/data.json", default_data)
    
    printf(f"▓ §fYour plugin §6§n{name} §r§fhas successfully been created !\n§r▓ §fIt runs its commands with the prefix: §6{prefix} §8[command] <sub_command/arguments>")
    
    
    