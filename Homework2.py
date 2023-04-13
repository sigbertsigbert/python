# Создать список и заполнить его элементами различных типов данных.
# Реализовать проверку типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя,а указать явно, в программе.



list = [12, -77, 'magic', 9.5, 5.0-1.0j, None, False, b'text', b"some magic", ]
print(list)
for el in list:
    print(f'{el} is {type(el)}')

# Для списка реализовать обмен значений соседних элементов,
# т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

el_count = int(input("Введите количество элементов: "))
list = []
i = 0
el = 0
while i < el_count:
    list.append(int(input("Введите значение: ")))
    i += 1

for el in range(int(len(list)/2)):
        list[el], list[el + 1] = list [el + 1], list[el]
        el += 2
print(list)

#Пользователь вводит месяц в виде целого числа от 1 до 12.
#Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
#Напишите два варианта решения: через list и через dict.

# Когда я указывала seasons_dict = {'winter': 1,'spring': 2},
# то при в вводе месяца, который относится, например, к зиме, получала ответ None. Не понимаю почему:с

seasons_dict = {1 :'winter', 2:'spring', 3:'summer', 4:'autumn'}
month = int(input("Введите номер месяца: "))
if month == 12 or month == 1 or month == 2:
        print(seasons_dict.get(1))

elif month == 3 or month == 4 or month ==5:
    print(seasons_dict.get(2))

elif month == 6 or month == 7 or month == 8:
    print(seasons_dict.get(3))

elif month == 9 or month == 10 or month == 11:
    print(seasons_dict.get(4))
    print(seasons_list[3])

else:
    print("Вы ввели слишком большое число, месяца под таким номером не существует")

seasons_list = ['winter', 'spring', 'summer', 'autumn']
month = int(input("Введите номер месяца: "))
if month == 12 or month == 1 or month == 2:
    print(seasons_list[0])

elif month == 3 or month == 4 or month == 5:
    print(seasons_list[1])

elif month == 6 or month == 7 or month == 8:
    print(seasons_list[2])

elif month == 8 or month == 9 or month == 10:
    print(seasons_list[3])

else:
    print("Вы ввели слишком большое число, месяца под таким номером не существует")

#Пользователь вводит строку из нескольких слов,
#разделённых пробелами. Вывести каждое слово с новой строки.
#Строки необходимо пронумеровать. Если слово длинное,
#выводить только первые 10 букв в слове.

# не понимаю, как сделать проверку, чтобы пользователь мог ввести только предложение, а не одно слово.
# Первой идеей был поиск пробела в строке, но не поняла, как использовать str.find(' ')
my_str = str(input("Введите предложение: "))
a = my_str.split(' ')
for i, el in enumerate(a, 1):
    if len(el) > 10:
        el = el[0:10]
    print(f"{i}. - {el}")

# Реализовать структуру «Рейтинг», представляющую собой не
# возрастающий набор натуральных чисел
# (каждый элемент ряда меньше или равен предыдущему).
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

my_list = [9, 8, 5, 5, 1]
number = int(input("Введите число: "))
a = my_list.count(number)
for element in my_list:
    if a > 0:
        i = my_list.index(number)
        my_list.insert(i+a, number)
        break
    else:
        if number < my_list[len(my_list) - 1]:
            my_list.append(number) # добавляет элемент в конец списка
            break
        elif  number > element:
            b = my_list.index(element)
            my_list.insert(b, number)
print(my_list)



