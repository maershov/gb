# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
# и метод running (запуск). Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в
# указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить
# соответствующее сообщение и завершать скрипт.
import time
CONST_RED = 'Красный'
CONST_YELLOW = 'Желтый'
CONST_GREEN = 'Зеленый'
class TrafficLight:
    __color = [CONST_RED, CONST_YELLOW, CONST_GREEN]

    def running(self):
        for value in self.__color:
            print(value)
            if value == CONST_RED:
                time.sleep(7)
            elif value == CONST_YELLOW:
                time.sleep(2)
            elif value == CONST_GREEN:
                time.sleep(5)
            else:
                print("invalid value")
                exit(-1)

tl = TrafficLight()
tl.running()

# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу:
# длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна.
# Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т
#
class Road:
    _length: int
    _width: int

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

def RoadMass(Road, volume, massPerMetr):
    return Road._width * Road._length * volume * massPerMetr



r = Road(25, 5000)
totalMass = RoadMass(r, 0.005, 25)
print(totalMass)

# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
# реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
# атрибутов, вызвать методы экземпляров).


class Worker:
    name: str
    surname: str
    position: str
    _income: {}

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        return f'{self.surname} {self.name}'
    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')

p = Position("Ivan", "Ivanov", "CEO", 200000, 350000)
print(p.get_full_name())
print(p.get_total_income())

# 4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    speed: int
    color: str
    name: str
    is_police: bool

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Car has gone")

    def stop(self):
        print("Car has stopped")

    def turn(self, direction):
        print(f'Car turned to the {direction}')

    def show_speed(self):
        print(f'current speed: {self.speed}')

    def show(self):
        print(f'speed: {self.speed} color: {self.color} name: {self.name}, is_police: {self.is_police}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Car speed is {self.speed}, speed is over limit 60')
        else:
            print(f'current speed: {self.speed}')

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Car speed is {self.speed}, speed is over limit 40')
        else:
            print(f'current speed: {self.speed}')

c = Car(100, "black", "first", False)
tc = TownCar(70, "Yellow", "second", False)
wc = WorkCar(30, "White", "Third", True)
print(c.show(), tc.show(), wc.show())
c.show_speed()
tc.show_speed()
wc.show_speed()

# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
# и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого
# из классов метод должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет
# описанный метод для каждого экземпляра.

class Stationery:
    title: str

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.")

class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки 1: {self.title}')

class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки 2: {self.title}')

class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки 3: {self.title}')

stat = Stationery("Канцелярия")
pen = Pen("Карандаш")
pencil = Pencil("Ручка")
handle = Handle("Маркер")
stat.draw()
pen.draw()
pencil.draw()
handle.draw()