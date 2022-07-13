import re
dict = {}
with open("old6.txt") as file:
    for line in file:
        name, hours = line.split(':')
        listnum = re.findall('[0-9]+', hours)
        numbers = [int(el) for el in listnum]
        dict[name] = sum(numbers)
print(f"{dict}")
