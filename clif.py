import sys, os, time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src" / "packages"))


import src.core as Core


def main():
    
    if len(sys.argv) > 1:
        original_dir = sys.argv[1]
    else:
        original_dir = os.getcwd()  # fallback

    SCRIPT_DIR = "C:\\Users\\roft\\Documents\\GitHub\\CLI-Fortress\\clif.py"
    sys.path.insert(0, SCRIPT_DIR)
    # sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=30, cols=130))

    Core.main(time.time(), original_dir)

if __name__ == "__main__": 
    main()