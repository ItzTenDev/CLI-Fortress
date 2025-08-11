import os
import shutil
import sys
import tempfile
import time
import subprocess

INSTALL_DIR = os.path.join(os.environ.get("LOCALAPPDATA", os.path.expanduser("~")), "CLI-Fortress")
WINDOWS_APPS = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft", "WindowsApps")


def uninstall():
    print("Uninstalling CLIF...")
    print("Removing clif.bat...")
    try: 
        os.remove(os.path.join(WINDOWS_APPS, "clif.bat"))
    except Exception as e: 
        print(f"Error removing clif.bat : {e}")

    print("Removing CLIF tool root...")
    try:
        os.rmdir(INSTALL_DIR)
    except Exception as e: 
        print(f"Error removing the Tool root : {e}")

    exit()
    

if __name__ == "__main__":
    uninstall()
