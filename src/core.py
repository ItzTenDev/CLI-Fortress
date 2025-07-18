# Nameless imports for quick access
from src.modules.formated_terminal import *

# Modules imports
import src.modules.terminal as terminal

import src.handlers.command_handler as command_handler
import src.modules.json_edit as json_edit


global_settings = json_edit.read("data/settings/global_settings.json")


# TO READ BEFORE USING OR EDITTING
# 
# You need to have NerdFont installed. Of course, no need to install it for your whole PC. Just apply to the terminal at least.
# If you're on VSCode, you need to set the "Terminal > Intergrated: Minimum Contrast Ratio" to 1, later if you want you can set it to 4.5
# 


def main():
    # Terminal Preparation
    terminal.run_command("cls")
    colors = [(0, 255, 255), (255, 0, 255)]

    print("\n".join([center_str(i) for i in get_ascii("HELLO WORLD", colors, darkening_factor=0.5)]) + "\n")
    printg("I love bananas", colors, True)
    

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
        
        exec_symbol = global_settings["__execution.display.data__"]["prefix_symbol"]
        terminal_size = os.get_terminal_size()

        input_command = input(int((terminal_size.columns - len(terminal_box[1])) // 2) * " " + "\033[1A" * 2 + f"│ {exec_symbol} ")

        
