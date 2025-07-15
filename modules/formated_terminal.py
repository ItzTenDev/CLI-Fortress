import os

ansi_notation = {
    # Formatting (unchanged)
    '§r': '\033[0m',   # RESET
    '§l': '\033[1m',   # Bold
    '§k': '\033[2m',   # Faint
    '§o': '\033[3m',   # Italic
    '§n': '\033[4m',   # Underline
    '§p': '\033[5m',   # Blink
    '§v': '\033[7m',   # Negative
    '§m': '\033[9m',   # Strikethrough

    # Red spectrum (softer variants)
    '§4': '\033[38;2;196;77;77m',    # Soft Dark Red
    '§4b': '\033[48;2;196;77;77m',   # Background
    '§c': '\033[38;2;255;136;136m',  # Soft Bright Red
    '§cb': '\033[48;2;255;136;136m', # Background

    # Orange/Yellow spectrum
    '§6': '\033[38;2;255;196;77m',   # Soft Gold
    '§6b': '\033[48;2;255;196;77m',  # Background
    '§e': '\033[38;2;255;255;136m',  # Soft Yellow
    '§eb': '\033[48;2;255;255;136m', # Background

    # Green spectrum
    '§2': '\033[38;2;77;196;77m',    # Soft Dark Green
    '§2b': '\033[48;2;77;196;77m',   # Background
    '§a': '\033[38;2;136;255;136m',  # Soft Bright Green
    '§ab': '\033[48;2;136;255;136m', # Background

    # Blue spectrum
    '§1': '\033[38;2;77;77;196m',    # Soft Dark Blue
    '§1b': '\033[48;2;77;77;196m',   # Background
    '§9': '\033[38;2;136;136;255m',  # Soft Bright Blue
    '§9b': '\033[48;2;136;136;255m', # Background

    # Cyan spectrum
    '§3': '\033[38;2;77;196;196m',  # Soft Dark Cyan
    '§3b': '\033[48;2;77;196;196m', # Background
    '§b': '\033[38;2;136;255;255m', # Soft Bright Cyan
    '§bb': '\033[48;2;136;255;255m',# Background

    # Purple/Magenta spectrum
    '§5': '\033[38;2;196;77;196m',  # Soft Dark Magenta
    '§5b': '\033[48;2;196;77;196m', # Background
    '§d': '\033[38;2;255;136;255m', # Soft Bright Magenta
    '§db': '\033[48;2;255;136;255m',# Background

    # Grayscale (softened)
    '§0': '\033[38;2;77;77;77m',     # Soft Black
    '§0b': '\033[48;2;77;77;77m',    # Background
    '§8': '\033[38;2;136;136;136m',  # Soft Dark Gray
    '§8b': '\033[48;2;136;136;136m', # Background
    '§7': '\033[38;2;196;196;196m',  # Soft Light Gray
    '§7b': '\033[48;2;196;196;196m', # Background
    '§f': '\033[38;2;255;255;255m',  # White (unchanged)
    '§fb': '\033[48;2;255;255;255m'  # Background
}

def print_color_samples(color_codes = ansi_notation):
    print("    Colors    |         RGB")
    print("--------------------------------------")
    
    for key, code in color_codes.items():
        # Skip non-color formatting codes (bold, underline, etc.)
        if ";2;" not in code:
            continue
            
        # Clean the ANSI code: remove ESC[ and trailing 'm'
        clean_code = code.replace("\033[", "").replace("m", "")
        parts = clean_code.split(";")
        
        # Extract RGB values (now safe from 'm' contamination)
        rgb = tuple(map(int, parts[2:5]))
        
        # Determine if foreground/background
        is_foreground = "38" in parts[0]
        color_type = "FG" if is_foreground else "BG"
        # Create colored block with padding
        print(
            code
            + f"{'######' if color_type == 'FG' else '      '}\033[0m {color_type} "
            + (key if color_type != 'FG' else key + ' ')
            + f" | \033[38;2;85;85;85m RGB: {rgb}"
        )

    print("\n\033[0m")  # Final reset


def color_verificator() -> None:
    final_str = ""
    index = 0
    for i in ansi_notation:
        if index % 2 != 0: final_str += ansi_notation[i] + "#\n\033[0m"
        else: final_str += ansi_notation[i] + "#\033[0m"
        index += 1
        
    print(final_str)


# Centers a string on the current terminal size
def center_str(string: str):
    x_cmd_size = os.get_terminal_size().columns
    
    spacers = int((x_cmd_size - len(string)) // 2) * " "
    return spacers + string + spacers


def printf(string: str, space_det : bool = True, center : bool = False) -> None:
    str_out = string[:]
    if center: str_out = center_str(str_out)

    for key in ansi_notation:
        value = ansi_notation[key]

        if key in string:
            if space_det : str_out = str_out.replace(key + " ", value)
            else : str_out = str_out.replace(key, value)

    print(str_out + "\033[0m")
    
    return