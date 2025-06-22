# CLI-Fortress

> A little OS in your terminal.

I’ve always found command-line interfaces (CLIs) super fun and cool.
So I decided to build my own little "OS" kind of CLI — just for fun. It’s not a real operating system (obiously), but more of a simulation, like... Kind of Lazyvim vibes in terms of design.
I just think that CLIs are so fun, like... Trying hard to make a good looking thing only using characters, that sound already super cool.

The idea behind this thing is to make something very **modular**. What i mean is that, you can add your own little tweaks to it, and it will handle the loading of those plugins/app by it self.
You don't have to recode the entire thing or hard-code your tweak inside the program, you just code your external program with some little mendatory files, and the CLI would recognize those.

Please, if you want to code your own app/plugin, please do, but try to not come out of the main idea : CLI.
It would be wierd to used tKinter for a CLI for example. But it is up to you. What could be fun is opening other CLIs as sort of "windows". That must be sick.

---

## Newest Features

> This section will be modified each time there is a new thing. It won't show every single feature, just the new ones.

So for now, it mostly has a command line system, which is the global thing, you can create custom commands and all. However, i need to create some global command system, like `[system/plugin] [command]` instead of directly having the command.
You can go to `src/commands/your_category/...` and add a `custom.py` command. DO NOT, give command names that already exist, and you MUST follow the constructor syntax with the `export()` function.

I think the next thing i will add soon is a "root command" property so we can add that `[system/plugin] [command]` thingy.

---

## Other Files

[Documentation](doc/DOCUMENTATION.md) - SOON

[TO-DO](TODO.md)
