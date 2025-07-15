from src.modules.formated_terminal import *

import src.modules.json_edit as json_edit
import src.modules.terminal as terminal

import importlib
import os


global_settings = json_edit.read("data/settings/global_settings.json")


# Finds command packs.
def pathload_command_packs(exceptions : list[str] = []) -> dict:
    cmd_pack_dir : str = global_settings["command_packs_directory"]
    command_packs_pathload = {}

    if not os.path.exists(cmd_pack_dir): # Check if the given path in the settings acctually exist
        terminal.print_err("CLIF_DEFAULT.CMD_PACK_DIR_NOT_FOUND", True)
    
    for (dir_path, dir_names, file_names) in os.walk(cmd_pack_dir):

        if 'data.json' in file_names: # This means that a command pack DATA has been found.
            cmd_pck_data = json_edit.read(dir_path + '/data.json')
            if cmd_pck_data["name"] in exceptions: continue

            command_packs_pathload[cmd_pck_data["prefix"]] = dir_path.replace("/", ".")
        else: continue
    
    return command_packs_pathload


# Find the command load path.
def pathload_commands(exceptions : list[str] = []) -> list[str]:
    cmds_load_paths : list[str] = []
    cmd_pack_dir : str = global_settings["command_packs_directory"]

    if not os.path.exists(cmd_pack_dir): # Check if the given path in the settings acctually exist
        terminal.print_err("CLIF_DEFAULT.CMD_PACK_DIR_NOT_FOUND", True)
    
    for (dir_path, dir_names, file_names) in os.walk(cmd_pack_dir):

        command_pack_name : str = ""

        if 'data.json' not in file_names: # This means that a command pack DATA has been found.
            continue
        else: 
            command_pack_name = json_edit.read(dir_path + "/data.json")["name"]
        
        if 'commands' in dir_names: # Checking if there is a cmd folder.
            cmds_path : str = dir_path + '/commands/'

            for entry in os.listdir(cmds_path):
                file_path = cmds_path + entry
                if os.path.isfile(file_path) and file_path.endswith(".py"): 
                    cmd_load_path = file_path.replace("/", ".").replace(".py", "")
                    cmds_load_paths.append(cmd_load_path)
        else: 
            terminal.print_warn("CLIF_DEFAULT.CMD_PCK_WITHOUT_CMDS", placeholders= {"%pack_name%": command_pack_name})

    return cmds_load_paths


def register_command_packs(exceptions : list[str] = []) -> None:
    register_path : str = global_settings["commands_pck_regstr_directory"]
    pathloads = pathload_command_packs(exceptions)

    json_edit.write(register_path, pathloads)
    terminal.print_success("CLIF_DEFAULT.CMD_PACKS_REGISTERED", placeholders= {"%registered_cmd_pck_count%": str(len(pathloads))})
    


def register_commands(exceptions : list[str] = []) -> None:
    pathloads : list[str] = pathload_commands(exceptions)
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