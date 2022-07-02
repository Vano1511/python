def capit(line): # функция преобразовывает строку
    capital_line = line.title()
    return capital_line
def capit1(line): # функция переделывает строку в список и редактирует его
    list_small = line.split()
    capital_list = []
    for el in list_small:
        capital_list.append(el.capitalize())
    #capital_list = " ".join(capital_list)  # если надо преобразовать список в строку обратно
    return  capital_list

line = input('введите солва через пробел ')

print(capit1(line)) # меняем фунцию, в зависимости, что хотим получить на выходе
