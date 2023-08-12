import utils


def main():
    raw_data = utils.get_json()
    sorted_by_date = utils.sort_by_date(raw_data)
    last_five_operations = utils.get_executed(sorted_by_date)
    got_date = utils.get_date(last_five_operations)
    for info in got_date:
        info["to"] = info["to"].split(" ")
        to = f'Счет **{info["to"][-1][-5:-1]}'
        if info.get("from"):
            info["from"] = info["from"].split(" ")
            if info['from'][0] == 'Счет':
                info['from'][-1] = f"**{info['from'][-1][-5:-1]} ->"
                from_ = ' '.join(info['from'])
            else:
                card_number = info['from'][-1]
                info['from'][-1] = f"{card_number[:4]} {card_number[5:7]}** **** {card_number[12:16]} ->"
                from_ = ' '.join(info['from'])
        if info.get('from'):
            print(f"""\n{info['date']} {info['description']}
{from_} {to}
{info['operationAmount']['amount']} {info['operationAmount']['currency']['name']}""")
        else:
            print(f"""\n{info['date']} {info['description']}
{to}
{info['operationAmount']['amount']} {info['operationAmount']['currency']['name']}""")


main()
