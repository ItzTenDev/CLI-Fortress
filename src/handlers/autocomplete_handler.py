from files import json_edit
from terminal import *

settings = json_edit.read("data/settings.json")

commands_register = json_edit.read(settings["commands_rgstr_directory"])
plugins_register = json_edit.read(settings["plugins_rgstr_directory"])


def fetch() -> list[str]:
    autocomplete_fetch = []

    # We register first the plugin prefix, because maybe the user only wants to write the plugin prefix and not a full command
    autocomplete_fetch += [prefix for prefix in plugins_register["__prefix__"]]


    # Same here, we first register commands before subcommands so the user gets only a command as a suggestion
    autocomplete_fetch += [plugins_register["__data__"][pathload.split(".")[2]]["prefix"] + " " + pathload.split(".")[4] for pathload in commands_register]

    for pathload in commands_register: 
        if commands_register[pathload]["sub_commands"] != {}:
            prefix = plugins_register["__data__"][pathload.split(".")[2]]["prefix"]
            command = pathload.split(".")[4]

            autocomplete_fetch += [" ".join([prefix, command, sub_command]) for sub_command in commands_register[pathload]["sub_commands"]]


    # Pathload.split(".")[0] = data
    # Pathload.split(".")[1] = plugins
    # Pathload.split(".")[2] = <plugin_id>
    # Pathload.split(".")[3] = commands
    # Pathload.split(".")[4] = <command_name>
    # 
    # commands_register[pathload]["sub_commands"] = {object_of_subcommands}
    # 
    # plugins_register["__data__"][<plugin_id>]["prefix"] = <plugin_prefix>
    #
    # command : plugin_prefix + command_name
    # command : plugins_register["__data__"][<plugin_id>]["prefix"] + " " + Pathload.split(".")[4]
    # command : plugins_register["__data__"][Pathload.split(".")[2]]["prefix"] + " " + Pathload.split(".")[4]

    return autocomplete_fetch
