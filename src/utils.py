import json


def get_json():
    with open("operations.json", "r", encoding="utf-8") as file:
        return json.load(file)


def sort_by_date(data):
    working_dicts = []
    for datum in data:
        if not datum:
            continue
        working_dicts.append(datum)
    sorted_input = sorted(working_dicts, key=lambda dict_to_sort: dict_to_sort['date'], reverse=True)
    return sorted_input


def get_executed(sorted_data):
    executed_list = []
    for one_list in sorted_data:
        if one_list['state'].lower() == 'executed':
            executed_list.append(one_list)
    five_only_list = []
    for n in range(0, 5):
        five_only_list.append(executed_list[n])
    return five_only_list


def get_date(lists):
    for list_ in lists:
        list_['date'] = list_['date'][0:10]
        list_['date'] = list_["date"].split("-")
        list_['date'] = f"{list_['date'][2]}.{list_['date'][1]}.{list_['date'][0]}"
    return lists
