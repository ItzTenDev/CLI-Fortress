from terminal import *

from files import json_edit

import time
import importlib
import os
import shlex


global_settings = json_edit.read("data/settings/global_settings.json")


# The command handler has a simple process.
# You first finds a loading path (which I call "pathload" go ask why) for each command and plugin which helps later for execution.
# This allows the REGISTER to put the infos in a json file to be able to load faster next time.
# 
# I haven't implemented it yet but, you might ask "yes but what if I update my command", and well, I thought of addind a version
# change system to plugins. If you update your plugin, you can simply change the version in your plugin data
# and the code will be like "hmmm the version changed, now I can load the whole thing back again"


# Retrives the loading root path of plugins
def pathfetch(exceptions: list[str] = []) -> dict:
    plugin_directory : str = global_settings["plugins_directory"]
    pathfetch_output : dict = {
            "__list__": [],
        }

    if not os.path.exists(plugin_directory): # Check if the given path in the settings acctually exist
        print_err("CLIF_DEFAULT.PLUGIN_DIR_NOT_FOUND", True)
        return {}
        
    for (dir_path, dir_names, file_names) in os.walk(plugin_directory):

        if 'data.json' in file_names: # This means that a plugin DATA has been found.
            plugin_data = json_edit.read(dir_path + '/data.json')  

            pathfetch_output[plugin_data["prefix"]] = dir_path.replace("/", ".") # Useful for command execution with prefix
            pathfetch_output["__list__"].append(dir_path.replace("/", ".")) # Useful for identifying what plugins are registered without iterating through the whole hashmap
        else: continue
        

    return pathfetch_output


# I am so funny. Please laugh. Command PACK... load_commands... C: I know, I know, peak humour right?
# Returns the loading paths of all the command of every registered plugin, exception excluded (lord I am so funny)
def load_commands(override: list[str] = [], exceptions: list[str] = []) -> list[str]: # D = 3
    load_commands_output = []
    plugins_register : dict = json_edit.read(global_settings["plugins_rgstr_directory"]) 

    for plugin in (plugins_register["__list__"] if override == [] else override): # Checks the override instead of register
        if plugin in exceptions: continue
        plugin_path = plugin.replace(".", "/")
        
        if not os.path.exists(plugin_path): # Does the path exist
            print_err("CLIF_DEFAULT.PLUGIN_PATH_NOT_FOUND", False, {"%pack_path%": plugin})
            continue;

        if not os.path.exists(plugin_path + "/data.json"): # Does data.json exist
            print_err("CLIF_DEFAULT.PLUGIN_DATA_NOT_FOUND", False, {"%pack_path%": plugin})
            continue;
    
        if not os.path.exists(plugin_path + "/commands"): # Does the command dir exist
            print_warn("CLIF_DEFAULT.CMD_PCK_WITHOUT_CMDS", placeholders= {"%pack_name%": plugin})
            continue;
    
        for entry in os.listdir(plugin_path + "/commands"): # Iterate to find commands
            file_path = plugin_path + "/commands/" + entry

            if os.path.isfile(file_path) and file_path.endswith(".py") and not entry.startswith("$"): # Assumes any python file in it is a command. Which is fine for later.
                cmd_load_path = file_path.replace("/", ".").replace(".py", "")
                load_commands_output.append(cmd_load_path)


    return load_commands_output # MUST contain a list of pathloads


def register_plugin(exceptions : list[str] = []) -> None:
    register_path : str = global_settings["plugins_rgstr_directory"]
    pathloads = pathfetch(exceptions)

    json_edit.write(register_path, pathloads)
    print_success("CLIF_DEFAULT.PLUGINS_REGISTERED", placeholders= {"%registered_plugin_count%": str(len(pathloads) - 1)})
    


def register_commands(exceptions : list[str] = [], process_time: float = 0) -> None:
    pathloads : list[str] = load_commands(exceptions)
    local_command_register = {}

    register_path : str = global_settings["commands_rgstr_directory"]

    printf("§e> §fLoading commands : §f[" + ("§0━"*20) + "§f]", False, end_str="\r")

    register_count = 0
    for pathload in pathloads:
        register_count += 1
        registered_proportion = (int((20 * register_count) / (len(pathloads))))

        printf("§e> §fLoading commands : §f[" + ((registered_proportion - 1) * "§6━") + "§6╸" + ("§0━"*(20 - registered_proportion)) + "§f]" + f" §r({pathload})" + " "*10, False, end_str="\r")

        time.sleep(process_time) # To slowly process the register

        command_data : dict = importlib.import_module(pathload).export()
        pathload_segments = pathload.split(".")
        command_name = pathload_segments[len(pathload_segments) - 1]
        
        nested_continue = False
        # Check if the requiredness is defined for all the arguments
        for arg in command_data["args"]:

            if not arg.startswith("r:") and not arg.startswith("o:"):
                print_err("CLIF_DEFAULT.CMD_ARGS_LACK_PREFIX", placeholders={"%cmd_name%": str(command_name)})
                nested_continue = True
                break;
        
        if nested_continue: continue
        

        # Check if the position requiredness is valid
        if not valid_positional_requiredness(command_data["args"]):
            print_err("CLIF_DEFAULT.CMD_ARGS_REQUIREDNESS_ORDER_INVALID", placeholders={"%cmd_name%": command_name})
            continue;


        local_command_register[pathload] = command_data

    print_success("CLIF_DEFAULT.CMDS_REGISTERED", placeholders= {"%registered_cmd_count%": str(register_count)})
    json_edit.write(register_path, local_command_register)


# Checks if the positions in order of the arguments is valid (meaning there should be no mendatory argument after the optional ones)
def valid_positional_requiredness(required_arguments: list[str]) -> bool:
    mendatory_limit : bool = False
    
    for arg in required_arguments: 
        if arg.startswith("o:"): mendatory_limit = True
        elif arg.startswith("r:") and mendatory_limit: return False

    return True


# Reads option argument section to be able to create a hash map of optional arguments.
def optional_argument_maper(given_arguments : list[str]):
    optional_map_output = {}
    
    for index in range(len(given_arguments)):
        arg = given_arguments[index]
        
        if arg.startswith("--"):
            optional_map_output[arg] = given_arguments[index + 1]
        elif arg.startswith("-"):
            optional_map_output[arg] = True

    
    return optional_map_output


# Execute command from name
def execute_command(input_command: str) -> None:
    plugins_register = json_edit.read(global_settings["plugins_rgstr_directory"])
    command_register = json_edit.read(global_settings["commands_rgstr_directory"])

        
    # Get the input data
    positional_parsing = shlex.split(input_command)
    plugin_prefix = positional_parsing[0]


    if len(positional_parsing) < 2:
        print_err("CLIF_DEFAULT.EXECUTION.PLUGIN_PREFIX_NOT_FOUND", placeholders={"%pack_prefix%": plugin_prefix})
        return


    if plugin_prefix not in plugins_register["__prefix__"]:
        print_err("CLIF_DEFAULT.EXECUTION.PLUGIN_PREFIX_NOT_FOUND", placeholders={"%pack_prefix%": plugin_prefix})
        return
    
    command = positional_parsing[1]
    pathload = ".".join([plugins_register["__prefix__"][plugin_prefix], "commands", command])


    # Check the input data
    if pathload not in command_register:
        print_err("CLIF_DEFAULT.EXECUTION.CMD_NOT_FOUND", placeholders={"%cmd_name%": plugin_prefix + " " + command})
        return
    
    command_import = command_register[pathload]

    is_sub_command = (len(positional_parsing) > 2) and (positional_parsing[2] in command_import["sub_commands"])
    arguments = positional_parsing[3 if is_sub_command else 2:]
    
    optional_arguments = optional_argument_maper(arguments)
    required_arguments = [arguments[index] for index in range(len(arguments)) if arguments[index] not in optional_arguments]

    root_command_import = command_import
    command_import = command_import["sub_commands"][positional_parsing[2]] if is_sub_command else command_import

    if len(required_arguments) < len([arg for arg in command_import["args"] if arg.startswith("r:")]):
        print_err("CLIF_DEFAULT.EXECUTION.CMD_ARGUMENT_LACKING", placeholders={
            "%cmd_name%": plugin_prefix + " " + command,
            "%usage%": " ".join([f"<{arg}>" for arg in command_import["args"]])
            })
        return

    root_pathload = pathload
    pathload = pathload.replace(f"commands.{command}", f"commands.{command_import["pathload_name"]}") if is_sub_command else pathload

    # Execute the command
    importlib.import_module(pathload).execute(required_arguments, optional_arguments, {"root": root_pathload, "pathload": pathload, "name": command, "root_data": root_command_import, "data": command_import})
    
    
    return

