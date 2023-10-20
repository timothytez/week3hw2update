import re

with open("./user_records.txt") as f:
    data = f.readlines()

    pattern = re.compile('([0-9]{2}), ([A-Za-z ]+)')

    true_ct = 0
    false_ct = 0

    for records in data:
        match = pattern.search(records)
        if match:
            ages = match.group(1)
            country = match.group(2)
            true_ct += 1
            print(f'Age: {ages}')
            print(f'Country: {country}')
        else:
            false_ct += 1

    print(f'Valid Count: {true_ct}\nInvalid Count: {false_ct}')