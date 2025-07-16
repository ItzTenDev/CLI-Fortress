import math 
from src.modules.formated_terminal import *
from src.modules.qk_diagrams import *

# Must be in every single command files.
def export() -> dict:
    name = "diagram"
    description = "I allow you to draw a circle !"
    args = ["LETTER:VALUE"]
    usage = name + "".join([" <" + arg + ">" for arg in args])
    permission = 0 
    
    return { "name" : name, "description" : description, "args" : args, "usage" : usage, "permission" : permission }


# Must be in every single command files.
def execute(user, args, database) -> None:
    raw_data_set = args[0:]
    data_set = []
    name_set = []
    
    for data in raw_data_set:
        data_chuncks = data.split(":")
        
        data_set.append(float(data_chuncks[1]))
        name_set.append(data_chuncks[0]) 
    
    diagram = Diagram(data_set, name_set)
    diagram.calc_aprox_delta()
    
    diagram.graph_offset = 2
    
    diagram.draw_diagram(-1, 5, 3)
    
    
    
    