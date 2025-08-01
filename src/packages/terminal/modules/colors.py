

ansi_notation = {
    # === Text formatting (style only, no color) ===
    '§r': '\033[0m',   # Reset all attributes
    '§l': '\033[1m',   # Bold
    '§k': '\033[2m',   # Faint (less bright)
    '§o': '\033[3m',   # Italic
    '§n': '\033[4m',   # Underline
    '§p': '\033[5m',   # Blink (slow)
    '§v': '\033[7m',   # Inverted / Negative
    '§m': '\033[9m',   # Strikethrough

    # === Red spectrum ===
    '§4db': '\033[48;2;98;38;38m',    # Darker variant (background)
    '§4d': '\033[38;2;98;38;38m',     # Darker variant (foreground)
    '§4b': '\033[48;2;196;77;77m',    # Background: Soft Dark Red
    '§4': '\033[38;2;196;77;77m',     # Foreground: Soft Dark Red

    '§cdb': '\033[48;2;128;68;68m',   # Darker variant (background)
    '§cd': '\033[38;2;128;68;68m',    # Darker variant (foreground)
    '§cb': '\033[48;2;255;136;136m',  # Background: Soft Bright Red
    '§c': '\033[38;2;255;136;136m',   # Foreground: Soft Bright Red

    # === Orange / Yellow spectrum ===
    '§6db': '\033[48;2;128;98;38m',
    '§6d': '\033[38;2;128;98;38m',    # Darker variant
    '§6b': '\033[48;2;255;196;77m',   # Background: Soft Gold
    '§6': '\033[38;2;255;196;77m',    # Foreground: Soft Gold

    '§edb': '\033[48;2;128;128;68m',
    '§ed': '\033[38;2;128;128;68m',   # Darker variant
    '§eb': '\033[48;2;255;255;136m',  # Background: Soft Yellow
    '§e': '\033[38;2;255;255;136m',   # Foreground: Soft Yellow

    # === Green spectrum ===
    '§2db': '\033[48;2;38;98;38m',
    '§2d': '\033[38;2;38;98;38m',     # Darker variant
    '§2b': '\033[48;2;77;196;77m',    # Background
    '§2': '\033[38;2;77;196;77m',     # Foreground: Soft Dark Green

    '§adb': '\033[48;2;68;128;68m',
    '§ad': '\033[38;2;68;128;68m',    # Darker variant
    '§ab': '\033[48;2;136;255;136m',  # Background
    '§a': '\033[38;2;136;255;136m',   # Foreground: Soft Bright Green

    # === Blue spectrum ===
    '§1db': '\033[48;2;38;38;98m',
    '§1d': '\033[38;2;38;38;98m',     # Darker variant
    '§1b': '\033[48;2;77;77;196m',    # Background
    '§1': '\033[38;2;77;77;196m',     # Foreground: Soft Dark Blue

    '§9db': '\033[48;2;68;68;128m',
    '§9d': '\033[38;2;68;68;128m',    # Darker variant
    '§9b': '\033[48;2;136;136;255m',  # Background
    '§9': '\033[38;2;136;136;255m',   # Foreground: Soft Bright Blue

    # === Cyan spectrum ===
    '§3db': '\033[48;2;38;98;98m',
    '§3d': '\033[38;2;38;98;98m',     # Darker variant
    '§3b': '\033[48;2;77;196;196m',   # Background
    '§3': '\033[38;2;77;196;196m',    # Foreground: Soft Dark Cyan

    '§bdb': '\033[48;2;68;128;128m',
    '§bd': '\033[38;2;68;128;128m',   # Darker variant
    '§bb': '\033[48;2;136;255;255m',  # Background
    '§b': '\033[38;2;136;255;255m',   # Foreground: Soft Bright Cyan

    # === Purple / Magenta spectrum ===
    '§5db': '\033[48;2;98;38;98m',
    '§5d': '\033[38;2;98;38;98m',     # Darker variant
    '§5b': '\033[48;2;196;77;196m',   # Background
    '§5': '\033[38;2;196;77;196m',    # Foreground: Soft Dark Magenta

    '§ddb': '\033[48;2;128;68;128m',
    '§dd': '\033[38;2;128;68;128m',   # Darker variant
    '§db': '\033[48;2;255;136;255m',  # Background
    '§d': '\033[38;2;255;136;255m',   # Foreground: Soft Bright Magenta

    # === Grayscale ===
    '§0db': '\033[48;2;38;38;38m',
    '§0d': '\033[38;2;38;38;38m',     # Darker Soft Black
    '§0b': '\033[48;2;77;77;77m',
    '§0': '\033[38;2;77;77;77m',      # Soft Black

    '§8db': '\033[48;2;68;68;68m',
    '§8d': '\033[38;2;68;68;68m',
    '§8b': '\033[48;2;136;136;136m',
    '§8': '\033[38;2;136;136;136m',   # Soft Dark Gray

    '§7db': '\033[48;2;98;98;98m',
    '§7d': '\033[38;2;98;98;98m',
    '§7b': '\033[48;2;196;196;196m',
    '§7': '\033[38;2;196;196;196m',   # Soft Light Gray

    '§fdb': '\033[48;2;128;128;128m',
    '§fd': '\033[38;2;128;128;128m',  # Dark White (neutral gray)
    '§fb': '\033[48;2;255;255;255m',
    '§f': '\033[38;2;255;255;255m',   # Pure White
}


# Colors
# > ItzTen
# 
# This one is just to make cool things using ansi color coding.
# Mainly for src.modules.formated_terminal



def gradient(colors, steps):
    if len(colors) < 2:
        raise ValueError("At least two colors are required.")
    
    segments = len(colors) - 1
    if steps % segments != 0:
        raise ValueError("Steps must be divisible by the number of color transitions (len(colors) - 1).")
    
    steps_per_segment = steps // segments
    gradient = []

    for i in range(segments):
        r1, g1, b1 = colors[i]
        r2, g2, b2 = colors[i + 1]
        
        for step in range(steps_per_segment):
            t = step / (steps_per_segment - 1) if steps_per_segment > 1 else 0
            r = int(r1 + (r2 - r1) * t)
            g = int(g1 + (g2 - g1) * t)
            b = int(b1 + (b2 - b1) * t)
    
    return gradient


def print_color_samples(color_codes = ansi_notation):
    print("    Colors    |         RGB")
    print("--------------------------------------")
    
    for key, code in color_codes.items():
        if ";2;" not in code:
            continue
            
        clean_code = code.replace("\033[", "").replace("m", "")
        parts = clean_code.split(";")
        
        rgb = tuple(map(int, parts[2:5]))
        
        is_foreground = "38" in parts[0]
        color_type = "FG" if is_foreground else "BG"
        print(
            code
            + f"{'######' if color_type == 'FG' else '      '}\033[0m {color_type} "
            + (key if color_type != 'FG' else key + ' ')
            + f" | \033[38;2;85;85;85m RGB: {rgb}"
        )



def darken_color(rgb, factor=0.35):
    return tuple(max(0, int(c * factor)) for c in rgb)


def colorf(string: str) -> str:
    str_out = string[:]

    for key in ansi_notation:
        value = ansi_notation[key]

        if key in string: str_out = str_out.replace(key, value)

    return (str_out + "\033[0m")
