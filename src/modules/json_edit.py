import json
import modules.terminal as terminal

from modules.colored_terminal import *

# Leave empty for reset
def write(path: str, data = []) -> int:
    with open(path, "w") as outfile:
        outfile.write(json.dumps(data, indent = 4))

    return 0

# To read files into python
def read(path: str):
    try:
        with open(path, "r") as infile:
            return json.load(infile)
    except: 
        printf("§f" + path + "§r not found", False)
        return
    

def set_property(path: str, new_value: dict):

    data : dict = read(path)
    data.update(new_value)

    write(path, data)
    return 0

    