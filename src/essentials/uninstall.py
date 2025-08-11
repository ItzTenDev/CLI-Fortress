import os
import shutil
import sys

def uninstall():
    # Absolute path to THIS uninstall.py
    self_path = os.path.abspath(__file__)
    essentials_dir = os.path.dirname(self_path)  # src/essentials
    install_dir = os.path.abspath(os.path.join(essentials_dir, "..", ".."))

    print("Uninstalling CLI-Fortress...")

    # Step 1: Remove everything except essentials/uninstall.py
    for root, dirs, files in os.walk(install_dir, topdown=False):
        for file in files:
            file_path = os.path.join(root, file)

            # Skip self until the end
            if os.path.abspath(file_path) == self_path:
                continue

            try:
                os.remove(file_path)
                print(f"Deleted file: {file_path}")
            except Exception as e:
                print(f"Failed to delete file {file_path}: {e}")

        for dir_ in dirs:
            dir_path = os.path.join(root, dir_)

            # Skip essentials folder until last
            if os.path.abspath(dir_path) == essentials_dir:
                continue

            try:
                shutil.rmtree(dir_path, ignore_errors=True)
                print(f"Deleted folder: {dir_path}")
            except Exception as e:
                print(f"Failed to delete folder {dir_path}: {e}")

    # Step 2: Delete essentials directory except self
    for file in os.listdir(essentials_dir):
        file_path = os.path.join(essentials_dir, file)
        if os.path.abspath(file_path) != self_path:
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    print(f"Deleted file: {file_path}")
                else:
                    shutil.rmtree(file_path, ignore_errors=True)
                    print(f"Deleted folder: {file_path}")
            except Exception as e:
                print(f"Failed to delete {file_path}: {e}")

    # Step 3: Delete self
    try:
        os.remove(self_path)
        print(f"Deleted uninstaller: {self_path}")
    except Exception as e:
        print(f"Failed to delete uninstaller: {e}")

    print("Uninstallation complete.")

if __name__ == "__main__":
    uninstall()
