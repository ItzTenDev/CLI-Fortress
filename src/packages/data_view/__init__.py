from .modules.qk_diagrams import *
from .modules.qk_tables import *

import data_view.modules.qk_diagrams as qk_diagrams
import data_view.modules.qk_tables as qk_tables


if __name__ == "__main__":
    test_table = Table(4, 4)
    test_table.draw_table