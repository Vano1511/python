def degree(num,deg):
    lenght = int(abs(deg))+1 # находим количество циклов
    num1 = num
    for el in range(lenght):
        num1 /= num
    print(round(num1,5))


# сначала проверка условий ввода
num = float(input('введите действительное положительное число х: '))
if num <= 0:
    print('число х должно быть больже нуля')
    exit()

deg = float(input('введите целое отрицательное число у : '))
if deg >= 0 or deg % 1 != 0:
    print('число у должно быть целым и отрицательным')
    exit()

# если все хорошо - возводим в степень
degree(num,deg)