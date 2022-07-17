rus_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре" }
with open('4out.txt', 'w') as new:
    with open('4in.txt', 'r') as old:
        for line in old:
            new.write(str(line.replace(line.split()[0], rus_dict.get(line.split()[0]))))



