import math 
from modules.colored_terminal import *


# Must be in every single command files.
def export() -> dict:
    name = "circle"
    description = "I allow you to draw a circle !"
    args = ["radius", "thickness"]
    usage = name + "".join([" <" + arg + ">" for arg in args])
    permission = 0 
    
    return { "name" : name, "description" : description, "args" : args, "usage" : usage, "permission" : permission }


# Must be in every single command files.
def execute(user, args, database) -> None:
    def draw_ascii_circle(radius, thickness):
        if radius <= 0 or thickness <= 0:
            raise ValueError("Radius and thickness must be positive integers.")

        output = []
        for y in range(-radius - thickness, radius + thickness + 1):
            row = ""
            for x in range(-2 * (radius + thickness), 2 * (radius + thickness) + 1):
                distance = math.sqrt((x / 2)**2 + y**2)  # Adjust x to account for character aspect ratio
                if radius - thickness <= distance <= radius:
                    row += "*"
                else:
                    row += " "
            output.append(row)
        return "\n".join(output)
    
    print(draw_ascii_circle(int(args[0]), int(args[1])))
    
    