import src.core as Core
import sys, os, time

if __name__ == "__main__": 
    # Get the absolute path to the libraries/ directory
    lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'src/packages'))

    # Add it to sys.path
    if lib_path not in sys.path:
        sys.path.insert(0, lib_path)
    

    # sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=30, cols=130))

    Core.main(time.time())