# class Example:
#     mode = []
#     color = 'green'
#     def __init__(self, value, name):
#         self.value = value
#         self.__name = name
#
#     def get_value(self):
#         return self.__name
#
#     @classmethod
#     def print_class_data(cls):
#         print('Атрибуты класса:',cls.mode, cls.color)
#
#     @staticmethod
#     def useful_function():
#         return 'результат работы очень важной функции'
#
#
# object = Example(100,'первый')
# # print(object.get_value())
# # print(Example.get_value(object))
# Example.print_class_data()
# print(Example.useful_function())
#


# class Cylinder:
#     __instance_count = 0
#     def __init__(self, diameter, height):
#         Cylinder.__instance_count +=1
#         self.__d = diameter
#         self.__h = height
#         self.__area = Cylinder.calculate_surface_area(self.__d, self.__h )
#     @staticmethod
#     def calculate_surface_area(d,h):
#         circle = 3.14 * (d/2) ** 2
#         side = 3.14 * d * h
#         return 2*circle + side
#     @classmethod
#     def total_instances(cls):
#         print('Создано сущностей:', cls.__instance_count)
#
# c = Cylinder(5,10)
# Cylinder.total_instances()
# print(c.calculate_surface_area(3,4))
# print(Cylinder.calculate_surface_area(4,5))

# import datetime
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @staticmethod
#     def is_adult(age):
#         if type(age) == int and 0<= age <=120:
#             return age >=18
#         return 'Неправильное значение атрибута'
#
#     @classmethod
#     def from_birth_year(cls, name, age):
#         return cls(name,datetime.datetime.now().year - age)
#
#     def __str__(self):
#         return f"{self.name} {self.age} лет"
#
# p1 = Person('Сережа', 20)
# print(p1.is_adult(p1.age))
# p2 = Person.from_birth_year('Баба Таня',1941)
# print(p2.age)
# print(p1)

# class MyStr:
#     def __init__(self,value):
#         self.value = value
#
#     def __mul__(self, other):
#         if type(other) == int:
#             result = ''
#             for i in range(other):
#                 result+= self.value
#             return result
#         elif type(other) == float:
#             other = round(other)
#             result = ''
#             for i in range(other):
#                 result += self.value
#             return result
#         else:
#             return 'Неправильный тип данных'
#
# s = MyStr('строка')
# print(s*4)
# print(s * 3.14)


# class Rectangle:
#     def __init__(self,area):
#         self.area = area

    # def __add__(self, other):
    #     return Rectangle(self.area  + other.area)
    # def __mul__(self, other):
    #     return Rectangle(self.area  * other.area)
#
# a = Rectangle(10)
# b = Rectangle(2)
# c = a+b
# print(type(c), c.area)
# d = a * b
# print(type(d), d.area)
# new = a+b+c+d



# class Rectangle:
#     def __init__(self,h,w):
#         self.h = h
#         self.w = w
#
#     @property
#     def get_area(self):
#         return self.h * self.w
#
# r = Rectangle(5,10)
# print(r.get_area)

class Item:
    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self,new_price):
        if type(new_price) in (float, int) and new_price > 0:
            self.__price = new_price
        else:
            print('неправильный ввод')
    @price.deleter
    def price(self):
        print('Атрибут удален')

print(Item.__dict__)