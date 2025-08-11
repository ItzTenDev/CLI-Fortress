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

## Newest Features

> This section will be modified each time there is a new thing. It won't show every single feature, just the new ones.

Now, you can run clif directly from your terminal using the command "clif" which will activate some environement vaariable for using some packages more quickly.

---

## Other Files

[Documentation](docs/DOCUMENTATION.md) - SOON
