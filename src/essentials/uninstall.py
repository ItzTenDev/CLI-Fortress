import os
import shutil
import sys
import tempfile
import time
import subprocess

def uninstall():
    self_path = os.path.abspath(__file__)
    essentials_dir = os.path.dirname(self_path)
    install_dir = os.path.abspath(os.path.join(essentials_dir, "..", ".."))

    print("Preparing uninstallation...")

    # Step 1: Create temp batch file outside install_dir
    temp_bat = os.path.join(tempfile.gettempdir(), "cli_fortress_uninstall.bat")

    with open(temp_bat, "w") as bat:
        bat.write(f"""@echo off
echo Uninstalling CLI-Fortress...
ping 127.0.0.1 -n 2 > nul
rmdir /s /q "{install_dir}"
echo Uninstallation complete.
del "%~f0"
""")

    print(f"Created temp uninstaller: {temp_bat}")

    # Step 2: Launch batch file AFTER this script exits
    subprocess.Popen(["cmd", "/c", temp_bat])

    # Step 3: Exit immediately so Python.exe can be deleted
    sys.exit()

if __name__ == "__main__":
    uninstall()
