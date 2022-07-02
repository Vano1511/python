def string_args(name,surname,yearbirth,city,email,phone):
    print(f'имя : {name}, фамилия : {surname}, год рождения : {yearbirth}, город проживания : {city},'
          f' е-mail : {email}, номер телефона : {phone}')

string_args(name=input('ввелите имя '),surname=input('введите фамилию '),yearbirth=input('введите год рождения '),
            city=input('введите город проживания '),email=input('введите е-mail '),phone=input('введите номер телефона '))

