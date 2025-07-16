from math import *
from src.modules.formated_terminal import *

import src.modules.terminal as terminal
import linecache

def get_cli(cli_name: str) -> list:
    return linecache.getlines("interfaces/" + cli_name + ".txt")


def display_cli(cli_name: str, with_data: dict):
    cli = get_cli(cli_name)
    full_print = ""
    
    for line in cli:
        to_print = str(line)
        
        for placeholder in with_data:
            to_print = to_print.replace(placeholder, str(with_data[placeholder]))
        
        full_print += to_print
        
    printf(full_print)
        
        
def update_cli(cli_name: str, with_data: dict):
    terminal.run_command("cls")
    display_cli(cli_name, with_data)