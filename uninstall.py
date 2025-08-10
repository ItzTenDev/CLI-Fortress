import os
import shutil
import stat

INSTALL_DIR = os.path.join(
    os.environ.get("LOCALAPPDATA", os.path.expanduser("~")),
    "CLI-Fortress"
)
LAUNCHER_BAT_PATH = os.path.join(
    os.environ["USERPROFILE"],
    "AppData", "Local", "Microsoft", "WindowsApps", "clif.bat"
)

def make_writable(path):
    """Remove read-only flag from file/folder."""
    try:
        os.chmod(path, stat.S_IWRITE)
    except Exception as e:
        print(f"Could not change permissions for {path}: {e}")

def force_remove_readonly(func, path, exc_info):
    """Error handler for rmtree to delete read-only files."""
    make_writable(path)
    try:
        func(path)
    except Exception as e:
        print(f"Error removing {path}: {e}")

def uninstall():
    # Remove installation folder
    if os.path.exists(INSTALL_DIR):
        print(f"Removing CLI-Fortress installation at:\n{INSTALL_DIR}")
        try:
            shutil.rmtree(INSTALL_DIR, onerror=force_remove_readonly)
            print("Installation folder removed.")
        except Exception as e:
            print(f"Error while uninstalling installation folder: {e}")
    else:
        print("CLI-Fortress installation folder not found.")

    # Remove launcher batch file
    if os.path.exists(LAUNCHER_BAT_PATH):
        print(f"Removing launcher batch file at:\n{LAUNCHER_BAT_PATH}")
        try:
            make_writable(LAUNCHER_BAT_PATH)
            os.remove(LAUNCHER_BAT_PATH)
            print("Launcher batch file removed.")
        except Exception as e:
            print(f"Error while removing launcher batch file: {e}")
    else:
        print("Launcher batch file not found.")

    print("Uninstallation complete.")
    exit()

if __name__ == "__main__":
    uninstall()
