true_password = 'qwerty'
try_account = 3
current_try = 1
success = False

while current_try <= try_account and not success:
    user_password = input('введите пароль - ')
    if user_password == true_password:
        success = True
        print('Пароль верный, доступ разрешен')
    else:
        print('пароль неверный, осталось попыток: ', try_ac123count-current_try)
        current_try = current_try + 1
    if current_try > try_account:
        print('попытки зончились, доступ запрещен')
