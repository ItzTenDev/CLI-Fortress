from modules.formated_terminal import *

import modules.json_edit as json_edit
import modules.terminal as terminal
import importlib

import clif
import os


command_packs_list = []


# Find the command load path.
def load_commands() -> list[str]:
    cmds_load_paths : list[str] = []
    cmd_pack_dir : str = clif.global_settings["command_packs_dir"]

    if not os.path.exists(cmd_pack_dir): # Check if the given path in the settings acctually exist
        terminal.print_err("CLIF_DEFAULT.CMD_PACK_DIR_NOT_FOUND", True)
    
    for (dir_path, dir_names, file_names) in os.walk(cmd_pack_dir):

        if 'data.json' in file_names: # This means that a command pack DATA has been found.
                cmd_pck_data = json_edit.read(dir_path + '/data.json')
                command_packs_list.append(cmd_pck_data["name"])
        else: continue
        
        if 'cmds' in dir_names: # Checking if there is a cmd folder.
            cmds_path : str = dir_path + '/cmds/'

            for entry in os.listdir(cmds_path):
                file_path = cmds_path + entry
                if os.path.isfile(file_path) and file_path.endswith(".py"): 
                    cmd_load_path = file_path.replace("/", ".").replace(".py", "")
                    cmds_load_paths.append(cmd_load_path)
        else: 
            terminal.print_warn("CLIF_DEFAULT.CMD_PCK_WITHOUT_CMDS")

    return cmds_load_paths


# Execute command from name
def execute_cmd(exe_cmd: str) -> None:
    pass