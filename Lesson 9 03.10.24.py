# class Parent:
#     def __init__(self,name):
#         self.name = name
#     def parent_method(self):
#         return 'parent method'
#
# class Child(Parent):
#     def __init__(self,name, value):
#         super().__init__(name)
#         self.value = value
#     def child_method(self):
#         return 'child_method'
#
# c = Child('Имя','значение')
# print(c.parent_method())
# print(c.child_method())
from gc import collect

from odbc import error


# class Vehicle:
#     def __init__(self, max_speed, mileage):
#         self.__max_speed = max_speed
#         self.mileage = mileage
#
#     @property
#     def max_speed(self): #геттер
#         return self.__max_speed
#     @max_speed.setter
#     def max_speed(self,new_max_speed):
#         if isinstance(new_max_speed,int) and 2 <= new_max_speed<=300:
#             self.__max_speed = new_max_speed
#         else:
#             print('Введено недопустимое значение')
#     @max_speed.deleter
#     def max_speed(self):
#         self.__max_speed = None
#
# class Bus(Vehicle):
#     def __init__(self, max_speed, mileage,
#                  name, max_capacity,
#                  occupied_places, ride_fare, cash = 0):
#         super().__init__(max_speed,mileage)
#         self.name = name
#         self.max_capacity = max_capacity
#         self.occupied_places = occupied_places
#         self.ride_fare = ride_fare
#         self.cash = cash
#
#     def add_passengers(self, passenger_count):
#         if self.max_capacity - self.occupied_places >= passenger_count:
#             self.occupied_places += passenger_count
#             self.collect_fare(passenger_count)
#         else:
#             print('Не хватает места для всех пассажиров')
#
#     def collect_fare(self,passenger_count):
#         self.cash = passenger_count * self.ride_fare
#
#     def seating_capacity(self):
#         print(f'Свободно {self.max_capacity - self.occupied_places} из {self.max_capacity}')
#
#
#
# class SchoolBus(Bus):
#     def __init__(self, max_speed, mileage,
#                  name, max_capacity,
#                  occupied_places, ride_fare, cash=0):
#         super().__init__(max_speed, mileage, name, max_capacity, occupied_places, ride_fare, cash = 0)
#         self.ride_fare = 0
#     def collect_fare(self, passenger_count):
#         print('Это бесплатный школьный автобус')
#
#
# # b = Bus(120, 1500,'Автобус междугородний 512', 60, 0, 2500)
# # b.seating_capacity()
# # b.add_passengers(30)
# # print(b.cash)
# # b.add_passengers(25)
# # b.add_passengers(10)
# # b.seating_capacity()
# s = SchoolBus(60, 400, 'Школьный автобус',50,0,0,0)
# s.add_passengers(10)
# s.add_passengers(50)
# s.seating_capacity()

#
# class Furniture:
#      def __init__(self,name):
#          self.name = name
#
# class PutInFurniture(Furniture):
#     def __new__(cls, *args, **kwargs): #защитить себя от создания экземпляров
#         if cls is PutInFurniture:
#             raise TypeError(f'Нельзя создавать экземпляры класса {cls.__name__}')
#         return object.__new__(cls)
#
#     def __init__(self, name):
#         super().__init__(name)
#         self.items_inside = list()
#
#     def put_inside(self, *items):
#         for item in items:
#             self.items_inside.append(item)
#
#
# class PutOnFurniture(Furniture):
#     def __new__(cls, *args, **kwargs): #защитить себя от создания экземпляров
#         if cls is PutOnFurniture:
#             raise TypeError(f'Нельзя создавать экземпляры класса {cls.__name__}')
#         return object.__new__(cls)
#
#     def __init__(self, name):
#         super().__init__(name)
#         self.items_on_top = list()
#
#     def put_on_top(self, *items):
#         for item in items:
#             self.items_on_top.append(item)
#
#
# class Table(PutOnFurniture):
#     def __init__(self,name,leg_count):
#         super().__init__(name)
#         self.leg_count = leg_count
#
#     def hold_hot_pot(self):
#         print('На стол поставили горячий чайник')
#
# class Shelf(PutInFurniture):
#     def __init__(self,name, hanger_count):
#         super().__init__(name)
#         self.hanger_count = hanger_count
#
#     def put_on_hanger(self):
#         print('На вешалку в шкафу повесили вещь')
#
# class Tumbochka(PutInFurniture, PutOnFurniture):
#     def __init__(self,name, power_socket_count):
#         super().__init__(name)
#         self.power_socket_count = power_socket_count
#
#     def put_in_power_socket(self):
#         print('В розетку тумбочки подключили устройство')
#
# new = Tumbochka('тумба у кровати',2)
# new.put_on_top('Телефон','книга')
# print(new.items_on_top)


#Если возникает RecursionError -проблема с именем атрибута. Он должен быть приватным __
class Demo:
    def __init__(self,name):
        self.__name = name #попробуйте убрать черточки у __name и увидите проблему
    @property
    def name(self):
        return self.name
    @name.setter
    def name(self,new_name):
        self.name = new_name
    @name.deleter
    def name(self):
        self.name = None

d = Demo('Новый')