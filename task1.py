def division(num1,num2):
    if num2 == 0:
        print(f'деление на {num2} невозможно!')
    else:
        print(f'{num1} поделить на {num2} равно {round(num1/num2,4)}')
division(float(input('ведите число, которое будем делить : ')), float(input('введите число, на  которое будем делить : ')))