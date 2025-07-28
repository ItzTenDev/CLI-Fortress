from src.modules.formated_terminal import *

import src.modules.json_edit as json_edit
import src.modules.cli_reader as clir


global_settings = json_edit.read("data/settings/global_settings.json")
plugin_register = json_edit.read(global_settings["plugins_rgstr_directory"])
command_register = json_edit.read(global_settings["commands_rgstr_directory"])


# Must be in every single command files.
def export() -> dict:
    parent = "plugin"

    return {"parent": parent}


# Must be in every single command files.
def execute(req_args : list[str], opt_args : dict = {}, suplementary : dict = {}) -> None:    
    plugin_id = req_args[0]
    command_name = opt_args.get("--command") or opt_args.get("--c") or "*"

    if plugin_id not in plugin_register:
        print("This plugin do not exist.")
        return
    
    if command_name != "*":
        command_pathload = (".".join([global_settings["plugins_directory"] + plugin_id, "commands", command_name])).replace("/", ".")
        
        print(command_pathload)

        if command_pathload not in command_register:
            print("Command not found")
            return
        
        plugin_path = plugin_register[plugin_id].replace(".", "/") + "/data.json"
        plugin_data = json_edit.read(plugin_path)

        plugin_name = plugin_data["name"]
        file_path = command_pathload.replace(".", "/") + ".py"

        command_permission = command_register[command_pathload]["permission"]
        command_description = command_register[command_pathload]["description"]


        clir.display_cli("$plugin help", {
            "%cmd%": command_name,
            "%file%": file_path,
            "%plugin%": plugin_name,
            "%perm%": command_permission,
            "%description%": command_description,

            "%c%": "§6"
        })
    
    else:
        plugin_path = plugin_register[plugin_id].replace(".", "/") + "/data.json"
        plugin_data = json_edit.read(plugin_path)

        plugin_name = plugin_data["name"]
        plugin_description = plugin_data["description"]
        plugin_prefix = plugin_data["prefix"]
        plugin_author = plugin_data["author"]
        print(suplementary)





