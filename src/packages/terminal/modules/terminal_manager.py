from src.modules.formated_terminal import *

import src.modules.json_edit as json_edit
import os


global_settings = json_edit.read("data/settings/global_settings.json")


# This module allows the user to control a bit more of the terminal it self
# This module also allows the use to print out notifications in a consistent manner instead of having manual prints all over the code.
# 
# Version : v1.0.0


# ------------------------------------------- Terminal Usage ------------------------------------------- 


# Runs a real command from the OS itself (TO ONLY DO IN WINDOWS FOR NOW!!)
def run_command(command: str):
    try:
        os.system(command)
    except:
        printf("§cERROR §r: This command does exist, or you have made a mistake writing it", False)


# --------------------------------------- Terminal Notifications --------------------------------------- 


# Chars
# ◉ ◯ ◎
# ▓ ○


# Prints an error based on its ID. (Funny)
def print_err(msg_id: str, deadly: bool = False, placeholders: dict = {}) -> None:
    messages : dict = json_edit.read(global_settings["messages_err_directory"])
    message : str = messages[msg_id] + " "*(os.get_terminal_size().columns - len(messages[msg_id]) - 5)

    for k in placeholders: message = message.replace(k, placeholders[k])

    if msg_id in messages: printf("§c▓ ERROR: §l§f" + msg_id + " §r- §f" + message, False)
    if deadly: exit()

# Prints an warning based on its ID. (Funny)
def print_success(msg_id: str, placeholders: dict = {}) -> None:
    messages : dict = json_edit.read(global_settings["messages_success_directory"])
    message : str = messages[msg_id] + " "*(os.get_terminal_size().columns - len(messages[msg_id]))

    for k in placeholders: message = message.replace(k, placeholders[k])

    if msg_id in messages: printf("§2▓ SUCCESS §r- §f" + message, False)


# Prints an warning based on its ID. (Funny)
def print_warn(msg_id: str, placeholders: dict = {}) -> None:
    messages : dict = json_edit.read(global_settings["messages_warn_directory"])
    message : str = messages[msg_id] + " "*(os.get_terminal_size().columns - len(messages[msg_id]))

    for k in placeholders: message = message.replace(k, placeholders[k])

    if msg_id in messages: printf("§6▓  WARNING: §l§f" + msg_id + " §r- §f" + message, False)