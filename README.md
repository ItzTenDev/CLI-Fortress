<img width="1758" height="334" alt="image" src="https://github.com/user-attachments/assets/69d40654-62a8-4483-b46b-2376ce7adb1d" />

A simple and easy to use tool to create your own terminal environement.

# Introduction

CLI are cool. Controlling your whole computer using just letters looks fun. However, I've always found it pretty *hard* to make custom commands. I mean, I did try to make bat files ect. But I never had a way to instantly setup a command to a "command database" to be able to execute it with a simple word. Plus, I always needed to code theses using the batch script language which is not always intuitive or very accessible. That is why I created CLIF, a basic tool that allows you to create custom commands, plugins, apps (cli apps), all in one place and using a language that is accessible to everyone : Python.

My goal behind this tool is to allow user to style the terminal more easily while also making his command, some people likes when something works but everyone loves when it works AND it is pretty. Packages like `curses` or `blessed` are sometimes a bit confusing and not very intuitive, even somethings like `prompt-toolkit` allows you to do a lot of things more easily but without enough customization except for few colors here and there.

Anyone can contribute (which explains why I made it in Python), even if it is by coding a plugin, a module, a package, anything that gives more freedom to user in order to let them code more commands, without making overwhelming function that has 30 parameters.

# How to install

Go to the release seciton and download the python installer. Once downloaded, just double click on it to run it in python (if python is not set as the default opener for .py file, do it manually by right clicking and pressing "open with" and then python).

For now, the tool is only available on Windows.
After the installation is complete, you can run the tool by just typing `clif` in your terminal.

# How to uninstall

Simply open the tool with `clif` and open the command line menu and type the command `$$uninstall`
The current process is pretty messy. But it will get better on next update.

# How to contribute

First of all, make sure you have python installed and that your **python is actually registered in the Windows PATH**.
If not, re install python and make sure to tick the box that allow you to set it as a Windows PATH.
That ensures that the "python" prefix is not "py" or "py3", which is the prefix used in the core file of the CLI.

Once you've forked and have the repo on your local machine, you need to set up a venv and install the dependencies.
```shell
python -m venv venv
pip install -r requirements.txt
```

After this, you have to keep in mind that the keyword "clif" is only available for the **users**, not the developpers. 
Let's say you have downloaded CLIF from the Github Releases. Now you'd have access to the CLI that is installed as a literal tool you can edit as a user.
MAKE SURE YOU ARE IN THE ROOT DIRECTORY, not outside, not inside a sub directory. Only in the root one you've cloned from your fork.

#### **If you are not coding on VS Code, do this:**
To code thing as a developper, you need to go to the root directory of the fork you've made and run `.\src\essentials\clif.bat` if you're in PowerShell, `src/essentials/clif.bat` if you're on CMD. Theses will set up the environement variables that will make your life so much easier when you code. Because it will:
- Set `src/packages` as a library, so you can access its packages and modules from ANYWHERE without having to type an entire path to get those.
- Set `.pycache` as a `__pycache__` "collector", making it easier for you to read your file tree.

#### **If you are on VS Code:**
You can, if everything works well, just run the CLI using:
```shell
python -m clif
```

Anyway, after this you can simply make PRs and yeah that's it.
What you should keep in mind is that `clif` does NOT execute the developper CLI, it executes (if installed) the user CLI.

# Dependencies

You will need to (optionaly) download a NerdFont. Any works as long as you download one. This makes the TUI look cooler.
Then, sometimes your terminal simply doesn't support this beauty of a CLI (Not targetting VS Code at all).
So to fix that, either use the default Windows terminal OR another program that seem to work perfectly fine and that also allow you to easily define a terminal font : Windows Terminal (Not default one, the one on Microsoft Store... unfortunately :c)

## Newest Features

> This section will be modified each time there is a new thing. It won't show every single feature, just the new ones.

Now, you can run clif directly from your terminal using the command "clif" which will activate some environement vaariable for using some packages more quickly.

---

## Other Files

[Documentation](docs/DOCUMENTATION.md) - SOON
