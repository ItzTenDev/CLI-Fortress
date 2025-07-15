import json

# Leave empty for reset
def write(path: str, data = []) -> int:
    with open(path, "w", encoding="utf-8") as outfile:
        outfile.write(json.dumps(data, indent = 4))

    return 0

# To read files into python
def read(path: str) -> dict: 
    try:
        with open(path, "r", encoding="utf-8") as infile:
            return json.load(infile)
    except:
        from src.modules.formated_terminal import printf  # Local import avoids circular import at module level
        printf("§f" + path + "§r not found", False)
        return {}
    

def set_property(path: str, new_value: dict) -> None:
    # new_value = {"key": "value"}
    data = read(path)
    if data is None:
        data = {}
    data.update(new_value)

    write(path, data)

