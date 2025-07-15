# Goal : Make easy Diagrams easily
# For now : only sticks diagrams
from modules.formated_terminal import *

class Diagram:
    name_set = []
    data_set = []
    
    graph_offset = 5
    aprox_delta = 0
    
    def __init__(self, data_set : list, name_set : list):
        self.data_set = data_set
        self.name_set = name_set
    
    def calc_aprox_delta(self) -> None:
        delta_s = 0
        
        data_set_copy = self.data_set[:]
        
        studied_set = list(sorted(data_set_copy))
        
        for data in list(enumerate(studied_set)):
            index = data[0]
            if index == 0: continue
            
            data_val = data[1]
            delta_s += data_val - studied_set[index - 1]
            
        equi_diff = int((studied_set[len(studied_set) - 1] - studied_set[0]) // 1)
        
        self.aprox_delta = (delta_s/len(self.data_set) - (studied_set[len(studied_set) // (equi_diff)])) // 1
            
    def draw_diagram(self, grad_factor : float = -1, thickness : int = 2, spacing : int = 2, g_space_out : int = 2):
        if grad_factor == -1: grad_factor = self.aprox_delta
        
        cl_displ = ""
        data_set_copy = self.data_set[:]
        
        height = int(4 + max(list(sorted(data_set_copy))) // grad_factor)
        name_line = ""
        
        # Aesthetic factor, it is just here to make sur the x-axis has the same length as the y-axis
        sqr_adjustment = (height + 3) * 2 - (1 + ((thickness + spacing) * len(self.name_set) + spacing))
        
        for level in range(height - 1, -1, -1):
            gard_value = int(grad_factor * level)
            d_value = str(gard_value) if level % g_space_out == 0 else ""
            
            # Adjust the graph offset to avoid errors 
            if self.graph_offset - len(d_value) < 0: self.graph_offset += (len(d_value) - self.graph_offset)

            # Display line graduations on the left
            cl_displ += d_value + (self.graph_offset - len(d_value))*" " + "   │" + spacing*" " if gard_value != 0.0 else d_value + (self.graph_offset - len(d_value))*" " + "  ─┼" + spacing*"─"
            
            # Display potential line value display
            for data in range(len(self.data_set)):
                if gard_value != 0.0:
                    if self.data_set[data] >= gard_value: cl_displ += "§6 #§r "*thickness + spacing*" "
                    else: cl_displ += spacing*" " + " "*thickness 
                else:
                    if self.data_set[data] >= gard_value: cl_displ += "§e =§r "*thickness + spacing*"─"
                    else: cl_displ += spacing*" " + " "*thickness
                    
                    # Display the lines of names
                    if self.data_set[data] >= gard_value: name_line += (self.name_set[data][0:thickness] + (thickness - len(self.name_set[data][0:thickness]))*" ") + " "*spacing 
                    else: name_line += spacing*" " + " "*thickness 
            
            if level != 0.0: cl_displ += "\n"
            elif level == 0.0: cl_displ += sqr_adjustment*"─" + "\n"
        

        cl_displ += "\n"*(self.graph_offset - 1) + "      " + " "*spacing + name_line
        printf(cl_displ)
        