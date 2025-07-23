from src.modules.formated_terminal import *

import importlib
import src.modules.terminal as terminal

# Must be in every single command files.
def export() -> dict:
    description = "Executes the cls command in command prompt."
    args = ["r:sub command"]
    permission = 0
    
    return { "description" : description, "args" : args, "permission" : permission }


# Must be in every single command files.
def execute(req_args : list[str], opt_args : dict = {}, suplementary : dict = {}) -> None:
    sub_command = req_args[0]

    __sub_commands__ = ["new"]

    if sub_command in __sub_commands__:
        sub_command_import = importlib.import_module(suplementary["pathload"].replace(f"commands.{suplementary["name"]}", f"commands.${suplementary["name"]} {sub_command}"))

        if opt_args == {}:
            print("Lack of arguments") # TEMPORARY
            return

        sub_command_import.execute(req_args[1:], opt_args, suplementary)
    else:
        print("Sub command doesn't exist")
        return

    