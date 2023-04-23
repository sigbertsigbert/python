#Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
#Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def divmod (*args):
    try:
        args_x = int(input("Введите делимое: "))
        args_y = int(input("Введите делитель: "))
        res = args_x / args_y
    except BaseException:
        return ("Вы не можете делить на ноль")

    return(res)

print(divmod())

#Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
#имя, фамилия, год рождения, город проживания, email, телефон.
#Функция должна принимать параметры как именованные аргументы.
#Осуществить вывод данных о пользователе одной строкой.



user_name = (input("Введите имя: "))
user_surname = (input("Введите фамилию: "))
user_year_of_birth = (input("Введите год рождения: "))
user_city = (input("Введите город: "))
user_email = (input("Введите e-mail: "))
user_phone = (input("Введите номер телефона: "))

def user_personal_info(name, surname,year_of_birth,city,email,phone):
    return ' '.join([
        "name: ", name,
        "surname: ", surname,
        "year of birth: ", year_of_birth,
        "city: ", city,
        "e-mail: ", email,
        "phone: ", phone, "."
        ])

print(user_personal_info(name=user_name,surname=user_surname,year_of_birth=user_year_of_birth,city=user_city,email=user_email,phone=user_phone))

#Реализовать функцию my_func(), которая принимает три позиционных аргумента
#и возвращает сумму наибольших двух аргументов.

def my_func(*args):
    args1 = int(input("Введите x: "))
    args2 = int(input("Введите y: "))
    args3 = int(input("Введите z: "))

    if args1 >= args2 > args3:
        return args1 + args2
    elif args3 >= args2 > args1:
        return args3 + args2
    elif args1 >= args3 > args1:
        return args1 + args3
    elif args2 >= args1 > args3:
        return args2 + args1
    elif args2 >= args3 > args1:
        return args2 + args3
    else:
        return ("Введите другие числа")

print(my_func())

#Программа принимает действительное положительное число x и целое отрицательное число y.
#Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
#При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

def my_func(x,y):
    #x = int(input("Введите x: ")),
    #y = int(input("Введите y: "))
    v1 = x ** y
    v2 = 1
    i = 1
    while i <= abs(y):
        v2 *= x
        i += 1

    return v1, 1/v2

print(my_func(3,-2))

#Программа запрашивает у пользователя строку чисел, разделённых пробелом.
#При нажатии Enter должна выводиться сумма чисел.
#Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
#Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
#Но если вместо числа вводится специальный символ, выполнение программы завершается.
#Если специальный символ введён после нескольких чисел,
#то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

result = 0
while True:
    my_line = input("Введите числа или S, чтобы увидеть сумму: ")
    tokens = my_line.split(" ")
    for token in tokens:
        try:
            number = float(token)
            result += number
        except:
            if token == 'S':
                print(f"Сумма чисел: {result}")
                break

            else:
                print(f"Cумма чисел {result}. Ошибка")
                exit()


#Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
#но с прописной первой буквой.
#Например, print(int_func(‘text’)) -> Text.

import re
def int_func(*args):
    word = input("Введите слова: ")
    match = re.fullmatch(r"[A-z]\w+", word)
    print(word.title() if match else "Вы использовали некорректные символы")
    return
int_func()



