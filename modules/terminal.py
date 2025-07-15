from modules.formated_terminal import *

import modules.json_edit as json_edit
import os
import clif

# This module allows the user to control a bit more of the terminal it self
# This module also allows the use to print out notifications in a consistent manner instead of having manual prints all over the code.
# 
# Version : v1.0.0


# --------------------------------------- Terminal Usage --------------------------------------- 

# Access the currently opened session in the CLI to be able to use the data that it has recorded so far
def get_session():
    return json_edit.read("data/register/session.json")


# OBSOLETE - Used to return an error code in the session data which could be accessed in real time using get_session()
def return_code(code: int):
    json_edit.set_property("data/register/session.json", {"previous_error_code": code})
    return
    

# Runs a real command from the OS itself (TO ONLY DO IN WINDOWS FOR NOW!!)
def run_command(command: str):
    try:
        os.system(command)
    except:
        printf("§cERROR §r: This command does exist, or you have made a mistake writing it", False)


# --------------------------------------- Terminal Notifications --------------------------------------- 

# Prints an error based on its ID. (Funny)
def print_err(err_id: str, deadly: bool = False, replace: dict = {}) -> None:
    messages : dict = json_edit.read(clif.global_settings["messages_err_dir"])
    message : str = messages[err_id]

    for (k, v) in replace: message.replace(k, v)

    if err_id in messages: printf("§c> " + err_id + " §r- §f" + message, False)
    if deadly: exit()


# Prints an warning based on its ID. (Funny)
def print_warn(err_id: str, replace: dict = {}) -> None:
    messages : dict = json_edit.read(clif.global_settings["messages_warn_dir"])
    message : str = messages[err_id]

    for (k, v) in replace: message.replace(k, v)

    if err_id in messages: printf("§6> " + err_id + " §r- §f" + message, False)