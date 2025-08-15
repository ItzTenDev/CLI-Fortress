from terminal import printf, run_command

import linecache

def get_cli(cli_name: str) -> list:
    return linecache.getlines("src/interfaces/" + cli_name + ".txt")


def display_cli(cli_name: str, with_data: dict = {}):
    cli = get_cli(cli_name)
    full_print = ""
    
    for line in cli:
        to_print = str(line)
        
        for placeholder in with_data:
            to_print = to_print.replace(placeholder, str(with_data[placeholder]))
        
        full_print += to_print
        
    printf(full_print)
        
        
def update_cli(cli_name: str, with_data: dict):
    run_command("cls")
    display_cli(cli_name, with_data)