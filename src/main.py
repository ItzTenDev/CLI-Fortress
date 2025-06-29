# Nameless imports for quick access
from modules.colored_terminal import *
from datetime import datetime

# Modules imports
import modules.terminal as terminal
import modules.json_edit as json_edit
import handlers.command_handler as cmd_handler

# Settings variables
session_error_code = 0
session_data = json_edit.read("data/register/session.json")
if session_data is not None and "sys_name" in session_data:
    cli_previous_name: str = str(session_data["sys_name"])
else:
    cli_previous_name: str = "DefaultName"  # Fallback value if not found

# To config as needed
session_ready_data = {
    "sys_name": cli_previous_name,
    "date": str(datetime.today())[0:9],
    "previous_error_code": session_error_code
}
json_edit.write("data/register/session.json", session_ready_data)


ASCII_Title = [
terminal.center_str(" ██████╗██╗     ██╗███████╗"),
terminal.center_str("██╔════╝██║     ██║██╔════╝"),
terminal.center_str("██║     ██║     ██║█████╗  "),
terminal.center_str("██║     ██║     ██║██╔══╝  "),
terminal.center_str("╚██████╗███████╗██║██║     "),
terminal.center_str(" ╚═════╝╚══════╝╚═╝╚═╝     ")
]


# Terminal Preparation
terminal.run_command("cls")
printf("\n".join(ASCII_Title))


# Handling events and commmands
command_handler = cmd_handler.load_commands()

# Ensure command_handler is a dictionary before accessing keys
if command_handler is dict:
    json_edit.set_property("data/register/session.json", {
        "l_cmds": command_handler.get("loaded_cmd", 0), # Count of loaded commands
        "r_cmds": command_handler.get("regstr_cmd", 0), # Count of registered commands
        "l_events": 0, # Not available yet
        "r_events": 0, # Not available yet
    })
else:
    json_edit.set_property("data/register/session.json", {
        "l_cmds": 0,
        "r_cmds": 0,
        "l_events": 0,
        "r_events": 0,
    })
printf("\n")


# Defining run commands functions
max_cmd_pc = 3 # The maximum amount of commands executable before the screen clears
cmd_pc = 0 # Counts how many commands have been executed, regardless of the success of them.

# Code starts here
while True:
    command_input = input("\n\033[97m$ \033[0m")
    
    cmd_pc += 1
    
    if cmd_pc == max_cmd_pc: 
        terminal.run_command("cls")
        print("\n\033[97m$ \033[0m" + command_input)
        cmd_pc = 0
        
    exection = cmd_handler.execute_cmd(command_input)
    

    # Ensure exection is subscriptable before using exection[0]
    if exection is (list, tuple) and len(exection) > 0:
        match exection[0]:
            case 304: printf(("§c# §r<<§f" + command_input + "§r>> is not recognized as an installed command."), False)
            case 301: 
                usage_info = exection[1]["usage"] if (len(exection) > 1 and exection[1] is not None and isinstance(exection[1], dict) and "usage" in exection[1]) else ""
                printf(("§c# §f" + command_input + "§r This command should be used : " + usage_info + " "), False)
    elif exection is int:
        # Handle the case where exection is just an int (error code)
        if exection == 304:
            printf(("§c# §r<<§f" + command_input + "§r>> is not recognized as an installed command."), False)
        elif exection == 301:
            printf(("§c# §f" + command_input + "§r This command should be used properly."), False)
    

