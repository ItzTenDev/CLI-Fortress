from src.modules.formated_terminal import *

import src.modules.dir_file as df
import src.modules.json_edit as json_edit


global_settings = json_edit.read("data/settings/global_settings.json")

# Must be in every single command files.
def export() -> dict:
    description = "Executes the cls command in command prompt."
    args = ["r:name", "o:--description"]
    
    return { "description" : description, "args" : args }


# Must be in every single command files.
def execute(req_args : list[str], opt_args : dict = {}, suplementary : dict = {}) -> None:
    name : str = req_args[0]
    description : str = opt_args.get("--description") or "Default description"

    df.make_dir(global_settings["plugins_directory"] + (name.lower().replace(" ", "_"))) # Make main dir
    df.make_dir(global_settings["plugins_directory"] + (name.lower().replace(" ", "_")) + "/commands/") # Make commands dir
    df.make_dir(global_settings["plugins_directory"] + (name.lower().replace(" ", "_")) + "/events/") # Make events dir

    # Making data.json
    default_data = {
        "name": name,
        "prefix": name.lower().replace(" ", "-"),
        "description": description,
        "author": "Whatever"
        }

    json_edit.write(global_settings["plugins_directory"] + (name.lower().replace(" ", "_")) + "/data.json", default_data)
    
    
    
    