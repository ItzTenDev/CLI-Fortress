from src.modules.formated_terminal import *
from src.modules.terminal import *

from src.modules.more_hashmap import *
from src.modules.more_array import *


# Format : "name": ["icon", "color", "text_color", "content"]
presets = {
    "repo.version"  : [" ", "§9b", "§f", "%clif.version%"],
    "repo.author"   : [" ", "§8b", "§f", "%github.user%" ],
    "repo.stars"    : [" ", "§9b", "§f", "%github.stars%"],
    "repo.licsence" : [" ", "§9b", "§f", "v1.0.0"],
    "repo.version"  : [" ", "§9b", "§f", "v1.0.0"],
}



# PINS - v1.0.0
# > ItzTen
# 
# This module allows you to display pins with icons. Like in github.
# To run a test : python -m src.modules.pins
# CHECK BOTTOM



# Returns a singular string with the whole formatted pin display
def pin_format(preset: str, placeholder: dict = {}) -> str:
    if preset not in presets: 
        print_err("CLIF_BUILT_IN.MODULES.PINS.PRESET_NOT_FOUND", placeholders={"%preset%": preset})
        return "<null preset>"
    
    icon = presets[preset][0]           # The icon that will be on the side
    color = presets[preset][1]          # The color of the pin itself
    text_color = presets[preset][2]     # The color of the content of the pin
    content = presets[preset][3]        # The content of the pin

    icon_part = "§fb§0" + " " + icon + " §r"
    text_part = "§r" + color + text_color + " " + placeholder_set(content, placeholder) + " §r"

    pin_format_output = icon_part + text_part

    return colorf(pin_format_output, False)


# Formats multiple pins in a beautiful display
def pin_display(pins: list[str]) -> list[str]:
    # Iterates through the list of pins
    # Will make packs of 3
    # Allign each pack

    pin_display_output : list[str] = []

    for pack in array_pack(pins, 3):
        pack = colorf(" ".join(pack))
        pin_display_output.append(center_str(pack))

    return pin_display_output
    


if __name__ == "__main__":
    pin1 = pin_format("repo.version")
    pin2 = pin_format("repo.version")
    pin3 = pin_format("repo.version")
    pin4 = pin_format("repo.version")
    pin5 = pin_format("repo.version")

    pin_list = [pin1, pin2, pin3, pin4, pin5]

    printf("\n\n".join(pin_display(pin_list)), False)