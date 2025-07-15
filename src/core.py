# Nameless imports for quick access
from src.modules.formated_terminal import *
import src.modules.json_edit as json_edit

# Modules imports
import src.modules.terminal as terminal
import src.handlers.command_handler as cmd_handler


ASCII_Title = [
center_str(" ██████╗██╗     ██╗███████╗"),
center_str("██╔════╝██║     ██║██╔════╝"),
center_str("██║     ██║     ██║█████╗  "),
center_str("██║     ██║     ██║██╔══╝  "),
center_str("╚██████╗███████╗██║██║     "),
center_str(" ╚═════╝╚══════╝╚═╝╚═╝     ")
]


def main():
    # Terminal Preparation
    terminal.run_command("cls")
    printf("\n".join(ASCII_Title))

    # Handling events and commmands
    cmd_handler.register_command_packs()
    cmd_handler.register_commands()

    # Get the register content

    # Handle input
    print("")

    while True:
        input_command = input(":: ")
        # Under construction
