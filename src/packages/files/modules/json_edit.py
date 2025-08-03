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
        print("> " + repr(path) + " not found")
        return {}
    

def set_property(path: str, new_value: dict) -> None:
    # new_value = {"key": "value"}
    data = read(path)
    if data is None:
        data = {}
    data.update(new_value)

    write(path, data)

