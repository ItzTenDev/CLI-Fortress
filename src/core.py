# Nameless imports for quick access
from src.modules.formated_terminal import *

# Modules imports
import src.modules.terminal as terminal

import src.handlers.command_handler as command_handler
import src.modules.json_edit as json_edit


global_settings = json_edit.read("data/settings/global_settings.json")


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
    command_handler.register_command_packs([])
    command_handler.register_commands([])

    # Handle input
    print("")

    while True:
        # Terminal Styling
        terminal_box = [
        "╭───────────────────────────────────────────────────────────────────────╮",
        "│                                                                       │",
        "╰───────────────────────────────────────────────────────────────────────╯"]

        for line in terminal_box: print(center_str(line))
        
        exec_symbol = global_settings["__execution__"]["prefix_symbol"]
        terminal_size = os.get_terminal_size()

        input_command = input(int((terminal_size.columns - len(terminal_box[1])) // 2) * " " + "\033[1A" * 2 + f"│ {exec_symbol} ")

        
