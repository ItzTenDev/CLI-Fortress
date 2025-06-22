from math import *
from modules.colored_terminal import *

import modules.json_edit as json_edit
import modules.terminal as terminal
import json
import importlib
import os

command_register_cache = {} # Temporary registered commands


# Scan and check if the command exists in the register
def check_register(cmd_name: str) -> tuple:
    with open("register\commands.json", "r") as infile:
        register  = json.load(infile)

    for cmd in register:
        cmd_c = register[cmd]
        if cmd_c["name"] == cmd_name: return (True, cmd_c["import_path"])
    
    return (False, None)


# Scan and check if the command exists in the loading
def check_existance(cmd_name: str) -> tuple:
    
    for commands in command_register_cache:
        commands_content = command_register_cache[commands]
        if commands_content["name"] == cmd_name: return (True, commands_content["cmd_path"])
    
    return (False, None)


# Scan directory to load only the python scripts 
def load_commands(_log: bool = False, error_sensitive: bool = False) -> int: 
    loaded_cmd = 0

    for (dir_paths, dir_names, files) in os.walk('commands'):
        for dir_name in dir_names:
            if dir_name == "__pycache__": continue
            for entry in os.scandir('commands/' + dir_name):
                
                cmd_category = dir_name
                                
                if entry.is_file() and entry.path.endswith(".py"):

                    cmd_file_name = entry.path.split("\\")[1]

                    data_grab = importlib.import_module("commands." + cmd_category + "." +  cmd_file_name.replace(".py", ""))
                    exported_data = data_grab.export()

                    exported_data["category"] = cmd_category
                    exported_data["cmd_path"] = str(entry.path)
                    exported_data["import_path"] = str("commands." + cmd_category + "." +  cmd_file_name.replace(".py", ""))

                    if check_existance(exported_data["name"])[0]:
                        printf(("§c> §rCouldn't load " + cmd_file_name + " : " + exported_data["name"] + " already exists in §6" + check_existance(exported_data["name"])[1]), False)
                        
                        if error_sensitive: return 1
                        else: continue

                    command_register_cache[exported_data["name"]] = exported_data

                    if _log: printf(("§a> §fLOADED : §r" + cmd_file_name), False)
                    loaded_cmd += 1
    
    printf("\n")
    printf(("§a# §f" + str(loaded_cmd) + "§r Commands have been loaded ! "), False, True)
    
    registered_cmd = register_commands()

    return {
        "loaded_cmd": loaded_cmd,
        "regstr_cmd": registered_cmd,
    }


# Scan directory to registeir them in database
def register_commands() -> int: 
    global command_register_cache
    
    if command_register_cache == []: return 1
    register_cmd = len(command_register_cache) # Number of registered commands
    
    cmd_to_json = json.dumps(command_register_cache, indent = 4)

    with open("register\commands.json", "w") as outfile:
        outfile.write(cmd_to_json)
    
    printf(("§a# §f" + str(register_cmd) + "§r Commands have been registered ! "), False, True)
    command_register_cache = [] # Reset to save memory
    
    return register_cmd


# Execute command from name
def execute_cmd(exe_cmd: str) -> int: # 3 : Command error
    cmd_no_args = exe_cmd.split(" ")[0]

    if check_register(cmd_no_args)[0] == False: 
        terminal.return_code(304) # 04 : Not found
        return (304, None)
    
    cmd_data = json_edit.read("register\commands.json")[next(filter(lambda d: d == cmd_no_args, json_edit.read("register\commands.json")), None)]
    args = exe_cmd.split(" ")[1:]

    if len(args) < (len(cmd_data["args"])): return (301, cmd_data) # 01 : No args

    data_grab = importlib.import_module(cmd_data["import_path"])


    data_grab.execute(terminal.get_session(), args, None)
    return (0, None)