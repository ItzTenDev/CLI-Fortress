from terminal import *
from style import *
from files import json_edit

# Modules imports
import src.handlers.command_handler as command_handler
import src.handlers.plugin_handler as plugin_handler


global_settings = json_edit.read("data/settings/global_settings.json")


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
display_name            : str = execution_display_config["display_name"]
display_subtitle        : str = execution_display_config["display_subtitle"]
display_description     : str = execution_display_config["display_description"]
display_license         : str = execution_display_config["display_license"]
display_git_repository  : str = execution_display_config["display_git_repository"]
display_version         : str = execution_display_config["display_version"]
display_authors         : list[str] = execution_display_config["display_authors"]

display_prefix_symbol   = execution_display_config["display_prefix_symbol"]



# TO READ BEFORE USING OR EDITTING
# 
# You need to have NerdFont installed. Of course, no need to install it for your whole PC. Just apply to the terminal at least.
# If you're on VSCode, you need to set the "Terminal > Intergrated: Minimum Contrast Ratio" to 1, later if you want you can set it to 4.5


def clif_display():
    
    # Terminal Preparation
    run_command("cls")

    print("")
    print("")

    colors = [
        (170, 220, 255),  # CLIF SKY BLUE
        (215, 150, 255),  # CLIF VIBRANT LAVENDER
        (255, 160, 210)   # CLIF VIBRANT SUNSET PINK
    ]


    # print(gradient(colors, len("██░      ██░      ██░  ░░░░░ ██░░░░   ██░   ██░██░░░██     ██░   ██░░░██  ██░░░░    ░░░░██░  ░░░░██░"))[31])

    if display_name: print("\n".join([center_str(i) for i in get_ascii(name, colors, darkening_factor=0)]) + "\n")
    if display_subtitle: printf("§8" + subtitle + "", True)
    if display_description: printf("§8" + description + "", True)
    if display_git_repository: printf("$clif.lav§n" + f"{git_repository}" + "\n", True)

    pin_stack = []

    if display_license: pin_stack.append(pin_format("repo.licence", {"%github.repo.license%": repo_license}))
    if display_version: pin_stack.append(pin_format("repo.version", {"%github.repo.version%": version}))
    if display_authors: 
        for author in authors: pin_stack.append(pin_format("repo.author", {"%github.user.name%": author}))
    
    printf("\n\n".join(pin_display(pin_stack, 5)) + "\n", False)


def main():
    

    # Handling events and commmands
    plugin_handler.register_plugins([])
    command_handler.register_commands([])

    default_suggestion_list = ["exit"]
    
    while True:

        clif_display()

        # Terminal Styling
        exec_symbol = global_settings["__execution.display.data__"]["prefix_symbol"]
        input_command = InputBar(
            placeholder="Enter Command...",
            prompt=f'{exec_symbol} ',
            color="$clif.lav",
            autocomplete=default_suggestion_list
            ).suggest()

        if input_command == "" or input_command.startswith(" "): continue
        if input_command == "exit": exit()


        # Execution
        err = True
        print()
        print()

        if not err:
            try:
                command_handler.execute_command(input_command)
            except:
                print_err("CLIF_DEFAULT.ABSTRACT_SOMETHING_WENT_WRONG")
        else:
            command_handler.execute_command(input_command)


        input('-> Press "Enter" to continue...')
        
