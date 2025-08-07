import os
from files import json_edit

from rich.text import Text
from terminal.modules.colors import *
from blessed import Terminal



FONT = json_edit.read(str(os.getenv("PYTHONPATH", "./src/packages")).replace("./", "") + f"/terminal/data/fonts.json")["clif.default"]
term = Terminal()


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


def get_spacer(string_size: int, ratio: int = 1):
    x_cmd_size = os.get_terminal_size().columns
    
    spacer = int((x_cmd_size - string_size) // (2*ratio))
    return spacer


# Prints using a given local color format
def printf(string: str = "", center : bool = False, end: str = "\n", flush: bool=False) -> None:
    return print(colorf(string), end= end, flush=flush) if not center else print(center_str(colorf(string)), end= end, flush=flush)


def inputf(prompt: str = "", placeholder: str = "", visible_limit: int | None = None, autocomplete: list[str] | None = None, required_output: bool = False) -> str:
    buffer = ""
    cursor = 0
    scroll_offset = 0
    last_render = ""
    last_suggestion = ""
    last_buffer = ""

    print()  # New line

    prompt_len = escape_length(prompt)

    with term.cbreak():
        while True:
            y = term.get_location()[0]

            # Scroll adjustment
            if visible_limit is not None:
                if cursor < scroll_offset:
                    scroll_offset = cursor
                elif cursor > scroll_offset + visible_limit:
                    scroll_offset = cursor - visible_limit
                visible_text = buffer[scroll_offset:scroll_offset + visible_limit]
            else:
                scroll_offset = 0
                visible_text = buffer

            content_width = visible_limit if visible_limit is not None else escape_length(visible_text)

            # Autocomplete only when buffer changes
            suggestion = ""
            if autocomplete and buffer != last_buffer:
                for word in autocomplete:
                    if word.startswith(buffer):
                        suggestion = word[len(buffer):]
                        break

                last_buffer = buffer
                last_suggestion = suggestion
            else:
                suggestion = last_suggestion

            # Build line only if rendering changes
            render = prompt
            if not buffer:
                render += f"§8{placeholder[:content_width]}"
            else:
                render += visible_text
                if suggestion and visible_limit is not None:
                    rem = suggestion[:max(0, visible_limit - len(visible_text))]
                    render += f"§8{rem}"

            if render != last_render:
                printf(term.move_yx(y, 0), end="")

                # Overwrite previous longer content
                extra_clear = max(0, len(last_render) - len(render))
                printf(render + (" " * extra_clear), end="", flush=True)

                last_render = render


            # Reposition cursor
            printf(term.move_yx(y, prompt_len + cursor - scroll_offset), end="", flush=True)

            key = term.inkey()

            if key.name == "KEY_ENTER":
                if required_output and (buffer.strip() == ""):
                    continue
                printf("")
                return buffer

            elif key.name in ("KEY_BACKSPACE", "KEY_DELETE") or key == '\x7f':
                if cursor > 0:
                    buffer = buffer[:cursor - 1] + buffer[cursor:]
                    cursor -= 1

            elif key.name == "KEY_LEFT":
                if cursor > 0:
                    cursor -= 1

            elif key.name == "KEY_RIGHT":
                if cursor < len(buffer):
                    cursor += 1

            elif key.name == "KEY_TAB" and autocomplete:
                for word in autocomplete:
                    if word.startswith(buffer):
                        buffer = word
                        cursor = len(buffer)
                        break
                
            elif key.is_sequence:
                continue

            elif key:
                buffer = buffer[:cursor] + key + buffer[cursor:]
                cursor += 1


# Returns a line by line ascii string in gradient/colored print
def get_ascii(text: str, colors: list[tuple]) -> list[str]:
    ascii_lines = ascii_text(text)
    width = max(len(line) for line in ascii_lines)

    # Generate horizontal gradient
    col_colors = gradient(colors, width)

    result_lines = []
    for y, line in enumerate(ascii_lines):
        result_line = ""
        for x, char in enumerate(line):
            r, g, b = col_colors[x]
            if char == " ":
                result_line += " "
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


