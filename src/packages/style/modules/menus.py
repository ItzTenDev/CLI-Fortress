import keyboard

from terminal import printf, center_str, colorf, escape_length
from files import json_edit

import os

global_settings = json_edit.read("data/settings/global_settings.json")


def __default__(): pass


class InputBar:
    
    def suggest(self, input_symbol: str = ">", color : str = "§6", size: int = 71, placeholder_message : str = "§8dType something here§r"):
        middle_size : int = size - escape_length(colorf(placeholder_message)) - len(input_symbol) - 2
        input_front_column = len(input_symbol)

        terminal_box = [
            colorf(f"{color}╭{"─" * size}╮"),
            colorf(f"{color}│ {" " * input_front_column}{" " * middle_size}{(placeholder_message)} {color}│"),
            colorf(f"{color}╰{"─" * size}╯")]


        for line in terminal_box: printf(line, True)
        
        terminal_size = os.get_terminal_size()
        
        input_result : str = input(colorf(int((terminal_size.columns - escape_length(terminal_box[1])) // 2) * " " + "\033[1A" * 2 + f"{color}│{colorf("§r")} {input_symbol} "))

        return input_result

class SelectMenu:
    # Universal Keycodes
    UP = 72
    DOWN = 80
    ENTER = 28

    def __init__(self, options: list[str], color: str = "§6"):
        self.options = options
        self.color = color
        self.current_index = 0


    def display_menu(self):
        for index in range(len(self.options)):
            option = self.options[index]
            printf(f"{self.color if self.current_index == index else ""}{index}. {option}", True)


    def refresh_menu(self):
        print("\033[1A" * (len(self.options) + 1))
        self.display_menu()


    def suggest(self, execution = __default__, *args, **def_args):
        self.display_menu()

        while True:
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN:
                keycode = event.scan_code
                match keycode:
                    case self.UP: self.current_index = (self.current_index - 1) % len(self.options)
                    case self.DOWN: self.current_index = (self.current_index + 1) % len(self.options)
                    case self.ENTER: return self.options[self.current_index]
                
                execution(*args, **def_args)
                
                if keycode in [self.UP, self.DOWN, self.ENTER]: self.refresh_menu()


class OptionMenu:
    # Universal Keycodes
    UP = 72
    DOWN = 80
    ENTER = 28
    SPACE = 57

    def __init__(self, options: list[str], color: str = "§6"):
        self.options = {f"{index}": {
            "name": options[index],
            "value": False
        } for index in range(len(options))}

        self.color = color
        self.current_index = 0


    def display_menu(self):
        for index in range(len(self.options)):
            option = self.options[str(index)]["name"]
            printf(f"{f"§f●§r" if self.options[str(index)]["value"] else f"§8○§r"} {self.color if self.current_index == index else ""}{index}. {option}", False)


    def refresh_menu(self):
        print("\033[1A" * (len(self.options) + 1))
        self.display_menu()


    def suggest(self, execution = __default__, *args, **def_args):
        self.display_menu()

        while True:
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN:
                keycode = event.scan_code
                match keycode:
                    case self.UP: self.current_index = (self.current_index - 1) % len(self.options)
                    case self.DOWN: self.current_index = (self.current_index + 1) % len(self.options)
                    case self.ENTER: return (self.options[str(self.current_index)]["name"], self.options[str(self.current_index)]["value"])
                    case self.SPACE: self.options[str(self.current_index)]["value"] = not self.options[str(self.current_index)]["value"]

                execution(*args, **def_args)

                if keycode in [self.UP, self.DOWN, self.ENTER, self.SPACE]: self.refresh_menu()



if __name__ == "__main__":
    print(" ")


    menu = OptionMenu(["Option 1", "Option 2", "Option 3", "Option 4"])
    choice = menu.suggest()
    print(choice)
