import os
import src.modules.json_edit as json_edit 

from rich.text import Text
from src.modules.colors import *


FONT = json_edit.read("src/modules/modules_data/formated_terminal/fonts.json")["clif.default"]


# Formated Terminal
# > ItzTen
# 
# A module to do fun things with the terminal.



def printg(text: str, colors: list[tuple[int, int, int]], center: bool = False) -> str:
    if len(colors) < 2:
        raise ValueError("At least two colors are required.")
    
    steps = len(text)
    segments = len(colors) - 1

    if steps % segments != 0:
        raise ValueError("Text length must be divisible by the number of color transitions (len(colors) - 1).")
    
    steps_per_segment = steps // segments
    result = []

    for i in range(segments):
        r1, g1, b1 = colors[i]
        r2, g2, b2 = colors[i + 1]

        for step in range(steps_per_segment):
            t = step / (steps_per_segment - 1) if steps_per_segment > 1 else 0
            r = int(r1 + (r2 - r1) * t)
            g = int(g1 + (g2 - g1) * t)
            b = int(b1 + (b2 - b1) * t)

            char_index = i * steps_per_segment + step
            char = text[char_index]
            result.append(f"\033[38;2;{r};{g};{b}m{char}\033[0m")
    
    output = center_str(''.join(result)) if center else ''.join(result)

    print(output)
    return output


# Returns the length of a version outside of any ansi escape code.
def escape_length(string: str) -> int:
    return len(Text.from_ansi(string).plain)


# Returns a line by line ascii print of a string.
def ascii_text(text: str, font=FONT):
    text = text.upper()
    lines = [""] * 6
    for char in text:
        if char not in font:
            raise ValueError(f"Character '{char}' not in font.")
        glyph = font[char]
        for i in range(6):
            lines[i] += glyph[i]
    return lines


# Centers a string on the current terminal size
def center_str(string: str, ratio: int = 1):
    x_cmd_size = os.get_terminal_size().columns
    
    spacers = int((x_cmd_size - escape_length(string)) // (2*ratio)) * " "

    return spacers + string


# Prints using a given local color format
def printf(string: str, center : bool = False, end_str: str = "\n") -> None:
    return print(colorf(string), end= end_str) if not center else print(center_str(colorf(string)), end= end_str)


# Returns a line by line ascii string in gradient/colored print
def get_ascii( text: str, colors: list[tuple], shadow_chars: tuple = (" ", "▀", "█", "▄"), darkening_factor: float = 0.2) -> list[str]:
    ascii_lines = ascii_text(text)
    height = len(ascii_lines)

    # Get one gradient color per row (as RGB tuples)
    row_colors = gradient(colors, height)

    result_lines = []
    for y, line in enumerate(ascii_lines):
        r, g, b = row_colors[y]
        result_line = ""
        for char in line:
            if char == " ":
                result_line += " "
            elif char in shadow_chars:
                dr, dg, db = darken_color((r, g, b), factor=(1 - darkening_factor))
                result_line += f"\033[38;2;{dr};{dg};{db}m{char}\033[0m"
            else:
                result_line += f"\033[38;2;{r};{g};{b}m{char}\033[0m"
        result_lines.append(result_line)

    return result_lines


def callout(content:str = "hello world", icon: str = "", main: str = "§e", second: str = "*"):
    background = main + "db" if second == "*" else second
    p = main + background
    callout_box = [
        p + "╭" + "─"*(len(content) + 2 + len(icon)) + "╮§r",
        p + "│ " + icon + p + "§f" + content + p + " │§r",
        p + "╰" + "─"*(len(content) + 2 + len(icon)) + "╯§r"]
    
    printf("\n".join(callout_box), False)


if __name__ == "__main__":
    callout("This is a cool callout", "\uf120  ", "§c")


