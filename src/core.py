from terminal import *
from style import *
from files import json_edit


# Modules imports
import time
import src.handlers.command_handler as command_handler
import src.handlers.plugin_handler as plugin_handler
import src.handlers.autocomplete_handler as autocomplete_handler


settings = json_edit.read("data/settings.json")


# Global settings quick access
execution_display_data      = settings["__execution.display.data__"]
execution_display_config    = settings["__execution.display.config__"]


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

exec_symbol = settings["__execution.display.data__"]["prefix_symbol"]




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

    if display_name: print("\n".join([center_str(i) for i in get_ascii(name, colors)]) + "\n")
    if display_subtitle: printf("§8" + subtitle + "", True)
    if display_description: printf("§8" + description + "", True)
    if display_git_repository: printf("$clif.lav§n" + f"{git_repository}" + "\n", True)

    pin_stack = []

    if display_license: pin_stack += [pin_format("repo.licence", {"%github.repo.license%": repo_license})]
    if display_version: pin_stack += [pin_format("repo.version", {"%github.repo.version%": version})]
    if display_authors: pin_stack += [pin_format("repo.author", {"%github.user.name%": author}) for author in authors]
    
    printf("\n\n".join(pin_display(pin_stack, 5)) + "\n", False)


def main(exec_time: float = 0, original_directory: str = ""):
    
    cd = original_directory

    # Handling events and commmands
    plugin_handler.register_plugins([])
    command_handler.register_commands([])
    autocomplete_handler.register()

    time.sleep(0.2)

    autocomplete_finder = json_edit.read(settings["autocomplete_rgstr_directory"])["__HAG__"]

    default_suggestion_list = ["exit"] + autocomplete_finder


    select_menu = OptionStack("OPTIONS", [
        StaticOption("Run Command", ""),
        StaticOption("Configuration", ""),
        StaticOption("Exit CLIF", ""),
    ], "$clif.lav", "centr", warp=4, seperation=1)

    completion_time = time.time() - exec_time


    
    input_bar = InputBar(
        placeholder="Enter Command...",
        prompt=f'{exec_symbol} ',
        color="$clif.lav",
        autocomplete=default_suggestion_list,
        decorator=f"§8{completion_time:.2f}s"
    )

    while True:

        clif_display()
        # Terminal Styling
        #         
        input_command = ""
        selection = select_menu.suggest()

        match selection:
            case "Run Command": input_command = input_bar.suggest()
            case "Configuration": exit()
            case "Exit CLIF": exit()
        

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
        
