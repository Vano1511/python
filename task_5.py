from random import randrange
with open('new5.txt','w+') as file:
    file.write(" ".join([str(randrange(100)) for el in range(500)]))
    file.seek(0)
    print(f'сумма всех чисел в файле {file.name} равна {sum(map(int, file.readline().split()))}')
