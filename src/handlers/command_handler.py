from src.modules.formated_terminal import *

import src.modules.json_edit as json_edit
import src.modules.terminal as terminal

import importlib
import os


global_settings = json_edit.read("data/settings/global_settings.json")


# The command handler has a simple process.
# You first finds a loading path (which I call "pathload" go ask why) for each command and command pack which helps later for execution.
# This allows the REGISTER to put the infos in a json file to be able to load faster next time.
# 
# I haven't implemented it yet but, you might ask "yes but what if I update my command", and well, I thought of addind a version
# change system to command packs. If you update your command pack, you can simply change the version in your command pack data
# and the code will be like "hmmm the version changed, now I can load the whole thing back again"


# Retrives the loading root path of command packs
def pathfetch(exceptions: list[str] = []) -> dict:
    command_pack_directory : str = global_settings["command_packs_directory"]
    pathfetch_output : dict = {
            "__list__": [],
        }

    if not os.path.exists(command_pack_directory): # Check if the given path in the settings acctually exist
        terminal.print_err("CLIF_DEFAULT.CMD_PACK_DIR_NOT_FOUND", True)
        return {}
        
    for (dir_path, dir_names, file_names) in os.walk(command_pack_directory):

        if 'data.json' in file_names: # This means that a command pack DATA has been found.
            cmd_pck_data = json_edit.read(dir_path + '/data.json')  
            if cmd_pck_data["name"] in exceptions: continue

            pathfetch_output[cmd_pck_data["prefix"]] = dir_path.replace("/", ".") # Useful for command execution with prefix
            pathfetch_output["__list__"].append(dir_path.replace("/", ".")) # Useful for identifying what command packs are registered without iterating through the whole hashmap
        else: continue
        

    return pathfetch_output


# I am so funny. Please laugh. Command PACK... unPACK... C: I know, I know, peak humour right?
# Returns the loading paths of all the command of every registered command pack, exception excluded (lord I am so funny)
def unpack(override: list[str] = [], exceptions: list[str] = []) -> list[str]: # D = 3
    unpack_output = []
    command_packs_register : dict = json_edit.read(global_settings["commands_pck_regstr_directory"]) 

    for command_pack in (command_packs_register["__list__"] if override == [] else override): # Checks the override instead of register
        if command_pack in exceptions: continue
        command_pack_path = command_pack.replace(".", "/")
        
        if not os.path.exists(command_pack_path): # Does the path exist
            terminal.print_err("CLIF_DEFAULT.CMD_PACK_PATH_NOT_FOUND", False, {"%pack_path%": command_pack})
            continue;

        if not os.path.exists(command_pack_path + "/data.json"): # Does data.json exist
            terminal.print_err("CLIF_DEFAULT.CMD_PACK_DATA_NOT_FOUND", False, {"%pack_path%": command_pack})
            continue;
    
        if not os.path.exists(command_pack_path + "/commands"): # Does the command dir exist
            terminal.print_warn("CLIF_DEFAULT.CMD_PCK_WITHOUT_CMDS", placeholders= {"%pack_name%": command_pack})
            continue;
    
        for entry in os.listdir(command_pack_path + "/commands"): # Iterate to find commands
            file_path = command_pack_path + "/commands/" + entry

            if os.path.isfile(file_path) and file_path.endswith(".py"): # Assumes any python file in it is a command. Which is fine for later.
                cmd_load_path = file_path.replace("/", ".").replace(".py", "")
                unpack_output.append(cmd_load_path)


    return unpack_output # MUST contain a list of pathloads


def register_command_packs(exceptions : list[str] = []) -> None:
    register_path : str = global_settings["commands_pck_regstr_directory"]
    pathloads = pathfetch(exceptions)

    json_edit.write(register_path, pathloads)
    terminal.print_success("CLIF_DEFAULT.CMD_PACKS_REGISTERED", placeholders= {"%registered_cmd_pck_count%": str(len(pathloads) - 1)})
    


def register_commands(exceptions : list[str] = []) -> None:
    pathloads : list[str] = unpack(exceptions)
    local_command_register = {}

    register_path : str = global_settings["commands_rgstr_directory"]

    printf("§e> §fLoading commands : §f[" + ("§r-"*20) + "§f]", False, end_str="\r")

    register_count = 0
    for pathload in pathloads:
        register_count += 1
        registered_proportion = (int((20 * register_count) / (len(pathloads))))

        printf("§e> §fLoading commands : §f[" + registered_proportion * "§6-" + ("§r-"*(20 - registered_proportion)) + "§f]" + f" §r({pathload})" + " "*10, False, end_str="\r")

        command_data = importlib.import_module(pathload).export()
        local_command_register[pathload] = command_data

    terminal.print_success("CLIF_DEFAULT.CMDS_REGISTERED", placeholders= {"%registered_cmd_count%": str(register_count)})
    json_edit.write(register_path, local_command_register)


# Execute command from name
def execute_cmd(exe_cmd: str) -> None:
    pass