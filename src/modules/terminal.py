from modules.colored_terminal import *

import modules.json_edit as json_edit
import os


def get_session():
    return json_edit.read("register/session.json")


def return_code(code: int):
    json_edit.set_property("register/session.json", {"previous_error_code": code})
    return


# Centers a string on the current cmd size
def center_str(string: str):
    x_cmd_size = os.get_terminal_size().columns
    
    spacers = int((x_cmd_size - len(string)) // 2) * " "
    return spacers + string + spacers
    

def run_command(command: str):
    try:
        os.system(command)
    except:
        printf("§cERROR §r: This command does exist, or you have made a mistake writting it", False)