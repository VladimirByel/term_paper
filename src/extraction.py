import json


def json_thing():
    with open("operations.json", "r", encoding="utf-8") as file:
        return json.load(file)
