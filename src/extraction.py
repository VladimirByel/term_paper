import json


def get_json():
    with open("operations.json", "r", encoding="utf-8") as file:
        return json.load(file)


def sort_data(data):
    working_dicts = []
    for datum in data:
        if not datum:
            continue
        working_dicts.append(datum)
    sorted_input = sorted(working_dicts, key=lambda dict_to_sort: dict_to_sort['date'])
    return sorted_input
