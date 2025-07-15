

class Table:
    content = []
    l_str_p_c = [] # Largest String per Column
    
    def __init__(self, line_size : int, col_size : int):
        for line in range(line_size):
            self.content.append([" " for i in range(col_size)])
            self.l_str_p_c = [1 for i in range(col_size)]
    
    
    # I am the most unefficient human being coders has ever seen
    def set_values(self, args : list = [0, 0, "Hi"]):
        lspc = self.l_str_p_c
        
        for mod in args:
            line = mod[0]
            col = mod[1]
            value = mod[2]
            
            self.content[line][col] = value
            if lspc[col] < len(value): lspc[col] = len(value)
    
    
    
    def draw_table(self, char_set = ["|", "-", "+"]):
        final_table_chars = ""
        longest_line = ""
        
        for line in range(len(self.content)):
            line_cont = self.content[line]
            line_frontcall = "| "
            
            line_separator = ""
            
            for col in range(len(line_cont)):
                col_cont = line_cont[col]
                
                line_frontcall += col_cont + " "*(self.l_str_p_c[col] - len(col_cont)) + " | "
            
            for char in line_frontcall[0: len(line_frontcall) - 1]:
                if char == "|": line_separator += "+"
                else: line_separator += "-"
            
            final_table_chars += line_separator + "\n"
            final_table_chars += line_frontcall + "\n"
            
            if len(longest_line) < len(line_separator): longest_line = line_separator
        
        final_table_chars += longest_line
        print(final_table_chars)

# Usage : set_values([[line, column, content], [..., ..., ...], ...])

