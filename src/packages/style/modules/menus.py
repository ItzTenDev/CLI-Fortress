import keyboard

from terminal import inputf, printf, get_spacer, colorf, escape_length, center_str
from files import json_edit

from data_struct import array_pack

import os

global_settings = json_edit.read("data/settings/global_settings.json")


def __default__(): pass



class InputBar:

    def __init__(self, title: str = "", color: str = "§f", placeholder : str = "Type things here...", size: int = 72, height: int = 1, allocated_space: int = 0, decorator: str = "", prompt: str = "Type : ", autocomplete: list[str] | None = None):

        self.title = title #" $clif.sbHELLO GUYS LOL "
        self.color = color
        self.size = size
        self.height = height
        self.prompt = prompt
        self.placeholder = placeholder

        self.allocated_space = allocated_space

        self.decorator = decorator
        self.decorator_size = escape_length(self.decorator)

        self.hypehns = (((self.size-2) - escape_length(colorf(self.title)) - 1) // 2) + 1
        self.inside_space = self.size - 2

        self.header = f"{self.color}╭{"─"*self.hypehns}{colorf(self.title + "§r")}{self.color}{"─"*self.hypehns}╮"
        self.body   = f"{self.color}│{" "*(self.inside_space - self.decorator_size - 1)}{self.decorator} {self.color}│"
        self.footer = f"{self.color}╰{"─"*self.hypehns}{"─"*self.hypehns}╯"

        self.autocomplete = autocomplete


    def suggest(self) -> str:
        printf(self.header, True)
        printf("\n".join([self.body for _ in range(self.height)]), True)
        printf(self.footer, True)
        
        print("\n" * self.allocated_space)

        printf("$*$*$*" + "$*"*(self.height + self.allocated_space + 1))

        # terminal_size = os.get_terminal_size()
        # spacers = int((terminal_size.columns - size) // (2*1))

        input_prompt = colorf(f"{self.color}│§r {self.prompt}")
        formatted_prompt = " "*get_spacer(self.size) + input_prompt

        result = inputf(formatted_prompt, 
                        placeholder=self.placeholder, 
                        visible_limit=(self.size - escape_length(input_prompt) - self.decorator_size - 4),
                        autocomplete=self.autocomplete,
                        required_output=True)
        
        return result

class Option:
    # Universal Keycodes
    LEFT = 75
    RIGHT = 77
    ENTER = 28
    SPACE = 57

    selected = True
    content = "Default Content"

    particle = "§8-§r"
    brackets = [" ", " "]
    CUSTOM_KEYBIND = -1


    def __init__(self, content: str = "Default Content", keybind: int = -1): 
        self.CUSTOM_KEYBIND = keybind
        self.content = content


    def option_display(self, color: str = "$clif.lav"):
        return f"§r{self.brackets[0]}§r {self.particle} {color if self.selected else ""}{self.content} §r{self.brackets[1]}§r"
    

    def set_selection(self, condition: bool = True): self.selected = condition
    def update_data(self): return


    def ENTER_action(self): return self.content   

    def SPACE_action(self): return

    def LEFT_action(self): return

    def RIGHT_action(self): return

    
    def input_action(self, keycode: int):
        if keycode == self.ENTER or keycode == self.CUSTOM_KEYBIND: return self.ENTER_action()
        elif keycode == self.SPACE: self.SPACE_action()
        elif keycode == self.LEFT: self.LEFT_action()
        elif keycode == self.RIGHT: self.RIGHT_action()

        self.update_data()
    
class CheckOption(Option):
    
    value = False
    particle = "§8○§r" if not value else "§f●§r"


    def SPACE_action(self):
        self.value = not self.value
        self.particle = "§8○§r" if not self.value else "§f●§r"

    
    def input_action(self, keycode: int):
        if keycode == self.ENTER: return self.ENTER_action()
        elif keycode == self.SPACE: return self.SPACE_action()

class MultiOption(Option):

    content_list = ["Default Content 1", "Default Content 2"]

    current_selection: int = 0
    particle = f"§8{current_selection + 1}§r"

    brackets = ["§8<", "§8>"]



    def __init__(self, content_list: list[str] = ["Default Content 1", "Default Content 2"], keybind: int = -1): 
        self.CUSTOM_KEYBIND = keybind
        self.content = content_list[self.current_selection]
        self.content_list = content_list

        self.update_data()

    
    def LEFT_action(self): self.current_selection = (self.current_selection - 1) % (len(self.content_list))

    def RIGHT_action(self): self.current_selection = (self.current_selection + 1) % (len(self.content_list))


    def update_data(self): 
        self.particle = f"§8{self.current_selection + 1}§r"
        self.content = self.content_list[self.current_selection]

        direction_indicator = len(self.content_list) - self.current_selection

        self.brackets[0] = "§8 " if direction_indicator == len(self.content_list) else "§8<"
        self.brackets[1] = "§8 " if direction_indicator == 1 else "§8>"

class StaticOption(Option):

    def __init__(self, content: str = "Default Content", keybind: int = -1): 
        self.content = content
        self.CUSTOM_KEYBIND = keybind

class OptionStack:
    # Universal Keycodes
    UP = 72
    DOWN = 80
    LEFT = 75
    RIGHT = 77
    ENTER = 28
    SPACE = 57
    ESCAPE = 1

    layout: str = "default"
    max_size: int = 10

    current_page = 0
    warp = 4


    def __init__(self, title: str = "DEFAULT TITLE", options: list[Option] = [], color: str = "§6", layout: str = "default", warp: int = 4):
        self.title = title
        self.options = options
        self.color = color

        self.current_index = 0
        self.layout = layout

        self.warp = warp

        self.set_max_size()


    def set_max_size(self): 
        for index in range(len(self.options)):
            option : Option = self.options[index]
            self.max_size = max(self.max_size, escape_length(option.option_display()) + 10)

        return self.max_size


    def apply_layout(self, option: Option, layout: str = "default"):
        content = colorf(option.option_display(self.color))
        key_display = (f"§8{chr(option.CUSTOM_KEYBIND)}§r" if option.CUSTOM_KEYBIND != -1 else "")

        if layout == "default": content = content + f"   §8({key_display}§8)§r"
        elif layout == "centr": content = center_str(content + f"   §8({key_display}§8)§r")
        elif layout == "centr_al_left": 
            spacer =  self.set_max_size() - escape_length(content) - escape_length(colorf(key_display))
            aligned_content = content + (" " * spacer) + colorf(key_display)

            content = center_str(aligned_content)

        return colorf(content)
        


    def display_menu(self):
        printf(f"§8< §f{self.title} ({self.current_page + 1}/{((len(self.options) - 1) // self.warp) + 1}) §8> ({self.current_index})", True)
        print()

        displayable = [(self.warp)*self.current_page + index for index in range(self.warp) if (self.warp)*self.current_page + index <= (len(self.options) - 1)]

        for index in displayable:
            option : Option = self.options[index]
            option.set_selection(self.current_index == index)
            printf(self.apply_layout(option, layout= self.layout))
        
        printf(( " "*100 + "\n")*(self.warp - len(displayable)), True)


    def refresh_menu(self):
        print("\033[1A" * ((self.warp) + 4))
        self.display_menu()


    def suggest(self, execution = __default__, *args, **def_args):
        self.display_menu()
        while True:
            available = [(self.warp)*self.current_page + index for index in range(self.warp) if (self.warp)*self.current_page + index <= (len(self.options) - 1)]

            self.CUSTOM_KEYBING = self.options[self.current_index].CUSTOM_KEYBIND
            event = keyboard.read_event(suppress=True)
            if event.event_type == keyboard.KEY_DOWN:
                keycode = event.scan_code

                match keycode:
                    case self.UP: 
                        self.options[self.current_index].set_selection(False)
                        self.current_index = self.current_page*self.warp + (((self.current_index - self.current_page*self.warp) - 1) % len(available))
                        self.options[self.current_index].set_selection(True)

                    case self.DOWN:
                        self.options[self.current_index].set_selection(False)
                        self.current_index = self.current_page*self.warp + (((self.current_index - self.current_page*self.warp) + 1) % len(available))
                        self.options[self.current_index].set_selection(True)

                    case self.ENTER: return self.options[self.current_index].input_action(keycode)

                    case self.CUSTOM_KEYBING: return self.options[self.current_index].input_action(keycode)
                    case self.ESCAPE: return {}

                    case self.LEFT: 
                        self.current_page = ((self.current_page - 1) % (((len(self.options) - 1) // self.warp) + 1))
                        
                        self.options[self.current_index].set_selection(False)
                        self.current_index = self.current_page*self.warp
                        self.options[self.current_index].set_selection(True)

                    case self.RIGHT: 
                        self.current_page = ((self.current_page + 1) % (((len(self.options) - 1) // self.warp) + 1))

                        self.options[self.current_index].set_selection(False)
                        self.current_index = self.current_page*self.warp
                        self.options[self.current_index].set_selection(True)


                
                self.options[self.current_index].input_action(keycode)
                execution(*args, **def_args)
                
                if keycode in ([self.UP, self.DOWN, self.ENTER, self.SPACE, self.RIGHT, self.LEFT] + [self.options[self.current_index].CUSTOM_KEYBIND]): self.refresh_menu()



if __name__ == "__main__":
    print(" ")

    menu = OptionStack("RANDOM STUFF", [
        StaticOption("MATHEMATICS"), 
        StaticOption("PHYSICS"), 
        StaticOption("CHEMISTRY"), 
        StaticOption("FRENCH"), 
        StaticOption("ENGLISH"),
        StaticOption("GEOGRAPHY"),
        StaticOption("BIOLOGY"),

        
        ], color="$clif.lav", layout="centr_al_left")
    
    choice = menu.suggest()
    print(choice)
