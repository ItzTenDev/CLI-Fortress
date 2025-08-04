from ..data.color_format import color_codes


COLORS = color_codes


# Colors
# > ItzTen
# 
# This one is just to make cool things using ansi color coding.
# Mainly for src.modules.formated_terminal



def gradient(colors, steps):
    if len(colors) < 2:
        raise ValueError("At least two colors are required.")
    
    segments = len(colors) - 1
    if steps < segments:
        raise ValueError("Steps must be at least equal to the number of transitions.")

    segment_lengths = [steps // segments + (1 if i < steps % segments else 0) for i in range(segments)]

    gradient = []
    for i, seg_len in enumerate(segment_lengths):
        r1, g1, b1 = colors[i]
        r2, g2, b2 = colors[i + 1]
        for step in range(seg_len):
            t = step / (seg_len - 1) if seg_len > 1 else 0
            r = int(r1 + (r2 - r1) * t)
            g = int(g1 + (g2 - g1) * t)
            b = int(b1 + (b2 - b1) * t)
            gradient.append([r, g, b])
    return gradient[:steps]



def print_color_samples(color_codes = COLORS):
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

    for key in COLORS:
        value = COLORS[key]

        if key in string: str_out = str_out.replace(key, value)

    return (str_out + "\033[0m")
