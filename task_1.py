with open('new.txt', 'w') as file:
    while True:
        line = input('Введите новую строку - ')
        if not line:
            print('файл создан')
            break
        file.write(f'{line}\n')
