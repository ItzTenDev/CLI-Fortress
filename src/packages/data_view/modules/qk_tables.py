from terminal import printf, colorf, escape_length

class Table:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.content = [["" for _ in range(cols)] for _ in range(rows)]
        self.col_widths = [1 for _ in range(cols)]

    def set_value(self, row: int, col: int, value: str = "null"):
        self.content[row][col] = colorf(value)
        self.col_widths[col] = max(self.col_widths[col], escape_length(colorf(value)))

    def draw_table(self):
        # Box-drawing characters
        v = "│"
        h = "─"
        tl = "╭"
        tm = "┬"
        tr = "╮"
        ml = "├"
        mm = "┼"
        mr = "┤"
        bl = "╰"
        bm = "┴"
        br = "╯"

        def draw_line(left, mid, right):
            line = left
            for i in range(self.cols):
                line += h * (self.col_widths[i] + 2)
                if i != self.cols - 1:
                    line += mid
            line += right
            return line

        # Build table
        result = draw_line(tl, tm, tr) + "\n"
        for r in range(self.rows):
            # Content line
            row_line = v
            for c in range(self.cols):
                content = colorf(self.content[r][c])
                space = self.col_widths[c] - escape_length(colorf(content))
                row_line += f" {content}{' ' * space} {v}"
            result += row_line + "\n"

            # Middle or bottom line
            if r != self.rows - 1:
                result += draw_line(ml, mm, mr) + "\n"
            else:
                result += draw_line(bl, bm, br)

        printf(result)

# Example usage
if __name__ == "__main__":
    t = Table(4, 4)
    t.set_value(0, 0, "Name")
    t.set_value(0, 1, "Age")
    t.set_value(0, 2, "Country")
    t.set_value(0, 3, "Score")
    t.set_value(1, 0, "Alice")
    t.set_value(1, 1, "21")
    t.set_value(1, 2, "Canada")
    t.set_value(1, 3, "82")
    t.set_value(2, 0, "Bob")
    t.set_value(2, 1, "19")
    t.set_value(2, 2, "France")
    t.set_value(2, 3, "91")
    t.set_value(3, 0, "Chloe")
    t.set_value(3, 1, "22")
    t.set_value(3, 2, "Japan")
    t.set_value(3, 3, "77")
    t.draw_table()
