import os
import shutil
import sys
import subprocess
import time

install_dir = os.path.join(os.environ["LOCALAPPDATA"], "CLI-Fortress")
essentials_dir = os.path.join(install_dir, "src", "essentials")
self_file = os.path.abspath(__file__)

def bar(done, total, length=40):
    pct = done / total
    filled = int(length * pct)
    sys.stdout.write(f"\rProgress: { '\033[38;2;198;175;255m█' * filled + '\033[38;2;136;136;136m-' * (length - filled) }\033[0m {pct*100:.1f}%")
    sys.stdout.flush()

def run_global():
    if "venv" in sys.executable.lower() or "scripts" in sys.executable.lower():
        subprocess.Popen([r"C:\Windows\py.exe", self_file])
        sys.exit()

def uninstall():

    launcher = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft", "WindowsApps", "clif.bat")
    if os.path.exists(launcher):
        try: os.remove(launcher)
        except: pass

    total = sum(len(files) for _, _, files in os.walk(install_dir)) or 1
    done = 0

    for root, dirs, files in os.walk(install_dir, topdown=False):
        if os.path.abspath(root) == os.path.abspath(essentials_dir):
            continue
        for f in files:
            try: os.remove(os.path.join(root, f))
            except: pass
            done += 1; bar(done, total)
        for d in dirs:
            shutil.rmtree(os.path.join(root, d), ignore_errors=True)

    if os.path.exists(essentials_dir):
        for f in os.listdir(essentials_dir):
            path = os.path.join(essentials_dir, f)
            if os.path.abspath(path) != self_file:
                try:
                    os.remove(path) if os.path.isfile(path) else shutil.rmtree(path, ignore_errors=True)
                except: pass
                done += 1; bar(done, total)

    bat = os.path.join(os.environ["TEMP"], "uninstall_tmp.bat") # Temporary bat because uninstall.py needs to delete ITSELF, duh.
    with open(bat, "w") as f:
        f.write(f'timeout /t 1 >nul\n'
                f'del "{self_file}" >nul 2>&1\n'
                f'rmdir /s /q "{install_dir}" >nul 2>&1\n')
        
    time.sleep(0.2)

    subprocess.run([bat], creationflags=subprocess.CREATE_NO_WINDOW)

    bar(total, total)
    print("\nDone.")

if __name__ == "__main__":
    print()
    run_global()
    uninstall()
    