from terminal import *

from files import json_edit
import cli_helper as clir


settings = json_edit.read("data/settings.json")
plugin_register = json_edit.read(settings["plugins_rgstr_directory"])
command_register = json_edit.read(settings["commands_rgstr_directory"])


# Must be in every single command files.
def export() -> dict:
    parent = "plugin"

    return {"parent": parent}


# Must be in every single command files.
def execute(req_args : list[str], opt_args : dict = {}, suplementary : dict = {}) -> None:    
    plugin_id = req_args[0]
    command_name = opt_args.get("--command") or opt_args.get("--c") or "*"

    if plugin_id not in plugin_register["__data__"]:
        print_err("CLIF.COMMAND.PLUGIN$DELETE.PLUGIN_PATH_NOT_FOUND")
        return
    
    plugin_data = plugin_register["__data__"][plugin_id]

    plugin_name = plugin_data["name"]

    if command_name != "*":
        command_pathload = (".".join([settings["plugins_directory"] + plugin_id, "commands", command_name])).replace("/", ".")
        

        if command_pathload not in command_register:
            print_err("CLIF_DEFAULT.EXECUTION.CMD_NOT_FOUND")
            return
        
        file_path = command_pathload.replace(".", "/") + ".py"

        command_permission = command_register[command_pathload]["permission"]
        command_description = command_register[command_pathload]["description"]


        clir.display_cli("$plugin help-cmd", {
            "%cmd%": command_name,
            "%file%": file_path,
            "%plugin%": plugin_name,
            "%perm%": command_permission,
            "%description%": command_description,

            "%c%": "§6"
        })
    
    else:

        plugin_description = plugin_data["description"]
        plugin_prefix = plugin_data["prefix"]
        plugin_author = plugin_data["author"]
        plugin_version = plugin_data["version"]
        plugin_path = plugin_data["file"]
        
        clir.display_cli("$plugin help-plg", {
            "%plugin_name%": f"{plugin_name} §8({plugin_id})",
            "%plugin_file%": plugin_path,
            "%plugin_author%": ", ".join(plugin_author),
            "%plugin_version%": plugin_version,
            "%plugin_prefix%": plugin_prefix,
            "%description%": plugin_description,

            "%c%": "§6"
        })





