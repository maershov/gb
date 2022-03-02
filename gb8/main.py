# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен
# извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу
# полученной структуры на реальных данных.
class Data:
    def __init__(self, day_month_year):
        # self.day = day
        # self.month = month
        # self.year = year
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def check(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2019 >= year >= 0:
                    return f'Верно'
                else:
                    return f'Неверный год'
            else:
                return f'Неверный месяц'
        else:
            return f'Неверный день'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)}'


today = Data('11 - 1 - 2001')
print(today)
print(Data.check(12, 4, 2022))
print(today.check(11, 13, 2011))
print(Data.extract('11 - 11 - 2011'))
print(today.extract('11 - 11 - 2020'))
print(Data.check(1, 11, 2000))

# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя
# программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class DivisionByZero:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Деление на ноль не разрешено")


div = DivisionByZero(10, 100)
print(DivisionByZero.divide_by_null(10, 0))
print(DivisionByZero.divide_by_null(10, 0.1))
print(div.divide_by_null(100, 0))


# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список
# только числами. Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит
# работу скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список с числами выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводе пользователем
# очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число.
# Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
# При этом работа скрипта не должна завершаться.

class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                val = int(input('Введите значения'))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Недопустимое значение")
                y_or_n = input(f'Еще одна попытка? Y/N ')

                if y_or_n == 'Y' or y_or_n == 'y':
                    print(try_except.my_input())
                elif y_or_n == 'N' or y_or_n == 'n':
                    return f'Выход'
                else:
                    return f'Выход'


try_except = Error(1)
print(try_except.my_input())

# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники
# (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
from datetime import datetime

class Warehouse:
    def __init__(self, title):
        self.title = title
        self.lists = {}
        self.give_lists = {}

    def take_to_wh(self, equipment):
        t = datetime.now()
        self.lists.update({equipment.serial_number:[equipment.title, self,t]})
        print('На склад '+self.title+' получено оборудование:'+ '' +equipment.title+' ,серийный номер - '+ str(equipment.serial_number)+', Дата:'
              + str(t.day)+'.'+str(t.month)+'.'+str(t.year))


    def give_to_wh(self, equipment, other):
        t = datetime.now()
        self.give_lists.update({equipment.serial_number: [equipment.title,other, t]})
        print('Передано оборудование:' + '' + equipment.title + ' ,серийный номер - ' + str(
            equipment.serial_number) + ', Дата:'
              + str(t.day) + '.' + str(t.month) + '.' + str(t.year))
        other.take_to_wh(equipment)


    def list_equipments(self):
        print('На склад '+self.title + ' получено оборудование:')
        print(self.lists)
        print('Общее количество: ', len(self.lists))
        print('Со склада '+self.title + ' выдано оборудование:')
        print(self.give_lists)
        print('Общее количество: ', len(self.give_lists))




class Equipment:
    def __init__(self, title, serial_number):
        self.title = title
        self.serial_number = serial_number

    def __str__(self):
        return str(self.title)

class Printer(Equipment):
    def __init__(self,title,serial_number, print_velocity):
        Equipment.__init__(self, title, serial_number)
        self.print_velocity = print_velocity

    def __str__(self):
        return  'Название модели:' + Equipment.__str__(self) + ' ,Параметры: ' + str(self.print_velocity)


class Scanner(Equipment):
    def __init__(self, title,serial_number,resolution):
        Equipment.__init__(self, title, serial_number)
        self.resolution = resolution

    def __str__(self):
        return  'Название модели:' + Equipment.__str__(self) + ' ,Параметры: ' + str(self.resolution)

class Copier(Equipment):
    def __init__(self, title,serial_number, addit):
        Equipment.__init__(self, title, serial_number)
        self.addit = addit

    def __str__(self):
        return  'Название модели:' + Equipment.__str__(self) + ' ,Параметры: ' + str(self.addit)



store1 = Warehouse('First warehouse')
store2 = Warehouse('Second warehouse')
a = Printer('HP',345678,100)
b = Scanner('Epson',123456,4000)
c = Copier('Brother',987654, 50)
d = Printer('HP',245678,200)

print(a)
print(b)
print(c)

store1.take_to_wh(a)
store1.take_to_wh(b)
store1.take_to_wh(c)
store1.take_to_wh(d)

store1.give_to_wh(a, store2)

store1.list_equipments()
store2.list_equipments()

# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и
# передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.


# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.


# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
# создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.
class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма z1 и z2 равна')
        return f'z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение z1 и z2 равно')
        return f'z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'z = {self.a} + {self.b} * i'


z_1 = ComplexNumber(1, -2)
z_2 = ComplexNumber(3, 4)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)

