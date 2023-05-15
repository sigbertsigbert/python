#Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
#«день-месяц-год». В рамках класса реализовать два метода.
#Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип к типу
#«Число». Второй, с декоратором @staticmethod,
#должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
#Проверить работу полученной структуры на реальных данных.

from math import floor
from typing import List, Tuple, Union


class Number(int):
    def __str__(self):
        return f"{self:02}"


class Date:
    date_attrs = ('day', 'month', 'year')

    def __init__(self, date: str, /):
        fragments = date.split('-')

        if not self.validate(*fragments):
            raise ValueError(f"{date} Некорректный формат")

        self.day, self.month, self.year = self.transform(fragments)

    def __iter__(self):
        for attr in self.date_attrs:
            yield self.__getattribute__(attr)

    @classmethod
    def transform(cls, date: Union[List[str], Tuple[str]]) -> List[Number]:
        return [Number(i) for i in date]

    @staticmethod
    def validate(*date: Union[List[str], Tuple[str]]) -> bool:
        try:
            day, month, year = [int(x) for x in date]
        except TypeError:
            return False

        bis_sextus = bool(not (year % 400 and year % 4) and year % 100)
        end_mon_day = 28 + (month + floor(month / 8)) % 2 + 2 % month + 2 * floor(1 / month)
        end_mon_day += bis_sextus if month == 2 else 0

        return all([1 <= day <= end_mon_day, 1 <= month <= 12, year >= 1970])

    def __str__(self):
        return f"Date is '{'-'.join([str(s) for s in self])}'"


if __name__ == '__main__':
    for date in ('01-12-2011', '01-12-1969', '29-02-2020', '29-02-2021'):
        try:
            print(Date(date))
        except ValueError as e:
            print(e)


#Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
#Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class DivisionByNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Нельзя делить на 0")


div = DivisionByNull(1000, 100)
print(DivisionByNull.divide_by_null(100, 0))
print(DivisionByNull.divide_by_null(200, 0.1))
print(div.divide_by_null(18303, 0))

#Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
#Проверить работу исключения на реальном примере.
#Запрашивать у пользователя данные и заполнять список необходимо только числами.
#Класс-исключение должен контролировать типы данных элементов списка.
class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        while True:
            try:
                val = int(input('Введите значения и нажимайте Enter - '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Недопустимое значение")
                y_or_n = input(f'Попробовать еще раз? Y/N ')

                if y_or_n == 'Y' or y_or_n == 'y':
                    print(try_except.my_input())
                elif y_or_n == 'N' or y_or_n == 'n':
                    return f'Пока!'
                else:
                    return f'Пока!'

try_except = Error(1)
print(try_except.my_input())


#Начните работу над проектом «Склад оргтехники».
#Создайте класс, описывающий склад.
#А также класс «Оргтехника», который будет базовым для классов-наследников.
#Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
#В базовом классе определите параметры, общие для приведённых типов.
#В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

class Storage:
    pass


class OfficeEquipment:
    vat = 0.13
    added_value = 2.0
    retail_rate = 1.3

    def __init__(
            self,
            eq_type: str,
            vendor: str,
            model: str,
            color: str,
            purchase_price: float,
    ):
        self.type = eq_type
        self.vendor = vendor
        self.model = model
        self.color = color

        self.purchase_price = purchase_price

        self.printable = True if self.type in ("printer", "xerox") else False
        self.scannable = True if self.type in ("scanner", "xerox") else False

    @property
    def retail_price(self):
        return self.wholesale_price * self.retail_rate

    @property
    def wholesale_price(self):
        return self.purchase_price * (1 + self.vat) * (1 + self.added_value)

    def __str__(self):
        return f"{self.type} {self.vendor} {self.model} ({self.color})"


class Printer(OfficeEquipment):
    printable = True
    scannable = False

    def __init__(self, *args):
        super().__init__('printer', *args)


class Scanner(OfficeEquipment):
    printable = False
    scannable = True

    def __init__(self, *args):
        super().__init__('scanner', *args)


class Xerox(OfficeEquipment):
    printable = True
    scannable = True

    def __init__(self, *args):
        super().__init__('xerox', *args)


if __name__ == '__main__':
    p1 = Printer("Model", "1111", "pink", 78302)
    print(p1)

#Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
#Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
#Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
#Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.c = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма c1 и c2:')
        return f'c = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение c1 и c2:')
        return f'c = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'c = {self.a} + {self.b} * i'


c1 = ComplexNumber(7, -1)
c2 = ComplexNumber(5, 2)
print(c1)
print(c1 + c2)
print(c1 * c2)