# # class Person:
# #     '''
# #     Справка по использованию класса
# #     '''
# #     age = 20
# #     name = 10
# #     def __init__(self,instanse_name:str, instanse_age:int):
# #         self.instance_age = instanse_age
# #         self.instance_name = instanse_name
# #
# #     def plus(self,a:int,b:int)->int:
# #         '''
# #         :param a:
# #         :param b:
# #         :return:
# #         '''
# #
# #         return a+b
# #
# # #Упражнение 2
# # print(*dir(Person),sep=', ')
# # print(dir(Person))
# # print(Person.__dict__)
#
#
# #упражнение 3
first.name, first.age, first.music = input().split()
print(first.name, first.age, first.music, sep=', ')
#
# #Упр.4
# class Book:
#     author = 'Айзек Азимов'
#     title = 'Я, робот'
#     release = 1950
#
# #Упр.5
# class Coder:
#     name = "Семён Дмитриев"
#     level = 'intern'
#     experience = "Low"
#     salary_per_hour = 10

# from types import FunctionType
#
# def func(a):
#     func.__dict__[a] = a**2
#
#     pass
#
# class Demo:
#     pass
# x = 10
# print(type(x))
# print(type(Demo))
# print(type(func))
# print(func.__globals__)
# print()
#
# lambda_demo = lambda x:x**2 #пример лямбда-функции
# #Пример создания функции "низкоуровневый"
# new_func = FunctionType(func.__code__, #байт-код функции func
#                         func.__globals__, #её параметры
#                         'func_name', #имя функции
#                         (10,) #кортеж с аргументами по-умолчанию
#  )
# code = compile('print("Работает, ура!")','__name__','eval')
# func = FunctionType(code, globals(),'name_of_func')
# help(compile)

# print(help(type))
# User = type('NameOfClass', (), {}) #() - родители для наследования, dict() - атрбиуты и методы
#
# class Student:
#     def __init__(self, name):
#         self.name = name
#
# class SuperStudent(Student):
#     school="Сириус"
#     @property
#     def info(self):
#         return f"{self.school}/{self.name}"
# Vladislava = SuperStudent('Владислава')
# print(Vladislava.info)
#
# CustomSuperStudent = type('CustomSuperStudent', #название
#                           (Student, ), #кортеж родительских классов
#                           {
#                               '__doc__': 'Описание класса супер-студент',
#                               'school':'Сириус',
#                               'info': property(lambda self: f"{self.school}/{self.name}")
#                           }
#  )
# CustomVladislava = CustomSuperStudent('Владислава')
# print(CustomVladislava.info)