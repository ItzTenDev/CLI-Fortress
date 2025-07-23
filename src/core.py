# Nameless imports for quick access
from src.modules.formated_terminal import *
from src.modules.pins import *

# Modules imports
import src.modules.terminal as terminal

import src.handlers.command_handler as command_handler
import src.handlers.plugin_handler as plugin_handler
import src.modules.json_edit as json_edit


global_settings = json_edit.read("data/settings/global_settings.json")


# TO READ BEFORE USING OR EDITTING
# 
# You need to have NerdFont installed. Of course, no need to install it for your whole PC. Just apply to the terminal at least.
# If you're on VSCode, you need to set the "Terminal > Intergrated: Minimum Contrast Ratio" to 1, later if you want you can set it to 4.5
# 


def main():
    # Global settings quick access
    execution_display_data      = global_settings["__execution.display.data__"]
    execution_display_config    = global_settings["__execution.display.config__"]


    # Print Settings
    name            = execution_display_data["name"]
    subtitle        = execution_display_data["subtitle"]
    description     = execution_display_data["description"]
    repo_license    = execution_display_data["license"]
    git_repository  = execution_display_data["git_repository"]
    version         = execution_display_data["version"]
    authors         = execution_display_data["authors"]


    # Print Settings
    display_name            = execution_display_config["display_name"]
    display_subtitle        = execution_display_config["display_subtitle"]
    display_description     = execution_display_config["display_description"]
    display_license         = execution_display_config["display_license"]
    display_git_repository  = execution_display_config["display_git_repository"]
    display_version         = execution_display_config["display_version"]
    display_authors         = execution_display_config["display_authors"]

    
    # Terminal Preparation
    terminal.run_command("cls")
    colors = [(0, 255, 255), (255, 0, 255)]

    if display_name: print("\n".join([center_str(i) for i in get_ascii(name, colors, darkening_factor=0.5)]) + "\n")
    if display_subtitle: printf("§8" + subtitle + "\n", True)
    if display_description: printf("§8" + description + "\n", True)
    if display_git_repository: printf("§3§n" + f"{git_repository}" + "\n", True)

    pin_stack = []

    if display_license: pin_stack.append(pin_format("repo.licence", {"%github.repo.license%": repo_license}))
    if display_version: pin_stack.append(pin_format("repo.version", {"%github.repo.version%": version}))
    if display_authors: 
        for author in authors: pin_stack.append(pin_format("repo.author", {"%github.user.name%": author}))
    
    printf("\n\n".join(pin_display(pin_stack, 5)) + "\n", False)
    

    # Handling events and commmands
    plugin_handler.register_plugins([])
    command_handler.register_commands([])


    # Handle input
    print("")
    display_prefix_symbol   = execution_display_config["display_prefix_symbol"]


    while True:
        # Terminal Styling
        terminal_box = [
        "╭───────────────────────────────────────────────────────────────────────╮",
        "│                                                                       │",
        "╰───────────────────────────────────────────────────────────────────────╯"]

        for line in terminal_box: print(center_str(line))
        
        exec_symbol = global_settings["__execution.display.data__"]["prefix_symbol"]
        terminal_size = os.get_terminal_size()

        input_command = input(int((terminal_size.columns - len(terminal_box[1])) // 2) * " " + "\033[1A" * 2 + f"│ {exec_symbol if display_prefix_symbol else ""} ")


        # Execution
        err = True
        print()
        print()

        if not err:
            try:
                command_handler.execute_command(input_command)
            except:
                terminal.print_err("CLIF_DEFAULT.ABSTRACT_SOMETHING_WENT_WRONG")
        else:
            command_handler.execute_command(input_command)


        pause = input("\n-> Press (Enter to continue):")
        
        

        
