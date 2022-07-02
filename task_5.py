def sum_list(list):
    int_list = [int(el) for el in list]
    return sum(int_list)

all_sum = 0
finish_list = []
while finish_list == []: # повторяем запрашивать, пока не будет введен знак "!"

    user_list = input('введите числа через пробелы, для окончания программы введите "!" : ').split()

    if '!' in user_list: # находим все цифры до знака "!" и заканчиваем подсчет
        for el in user_list:
            if el == '!':
                break
            finish_list.append(el) # заполняем финишный список
        all_sum += sum_list(finish_list)
        print(f'общая сумма всех введенных чисел равна : {all_sum} , конец подсчета')
        exit()


    all_sum += sum_list(user_list)
    print(f'общая сумма всех введенных чисел равна : {all_sum}')