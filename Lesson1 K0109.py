'''Класс и объект. Принципы ООП. ООП в Python'''


# dog = {
#     'name': 'Барбос',
#     'height': 50,
#     'weight': 20,
#     'food': 'сухой корм'
# }
# def run(object):
#     if 'name' in object:
#         print(f"{object['name']} бежит")
#     else:
#         print('Ошибка вызова')
#
# def eat(object):
#     print(f"{object['name']} кушает")
# run(dog)
# eat(dog)
# Описание класса, "чертеж"
# class Dog():
#     name = 'Барбос'
#     height = 50
#     weight = 20
#     food = 'сухой корм'
#
#
#     def run(self):
#         print(f"{self.name} бегает")
#
#     def eat(self):
#         print(f"{self.name} кушает")
#
#
# def walk_on_two_legs(name):
#     print(f"{name} Ходит на двух ногах")
#
# barbos = Dog()
# barbos.trick = walk_on_two_legs
# barbos.trick(barbos.name)
# barbos.run()
# barbos.eat()
# print('Имя:', barbos.name)
#
# dyna = Dog()
# dyna.name = 'Дина'
# print(dyna.name)
# print(barbos.name)
#
# dyna.favorite_toy = 'Мячик'
# print(dyna.favorite_toy)
# #print(barbos.favorite_toy) ошибка!
#
# #проверить принадлеежность к классу:
# print(isinstance(barbos, Dog))
# x = 10
# print(isinstance(x,float))



#
# def func(x):
#     '''
#     :param x: значение, возводимое в квадрат
#     :return:  результат возведения в квадрат
#     '''
#     #dict_name[x] = значение
#     if x in func.__dict__:
#         print('Уже было!')
#     else:
#         print('Еще не было!')
#         func.__dict__[x] = x**2
#     return func.__dict__[x]
# for i in range(10):
#     print(func(i))
#
# print(func(5))
# print(func.__dir__())



# import time
#
# c = 0
# def f(n):
#     global c
#     c+=1
#     if n in f.__dict__:
#         return f.__dict__[n]
#     else:
#         if n == 0:
#             f.__dict__[n] = 0
#             return 0
#         if n == 1:
#             f.__dict__[n] = 1
#             return 1
#         else:
#             res = f(n-1) + f(n-2)
#             f.__dict__[n] = res
#             return res
# start_time = time.time()
# print('Результат:',f(35))                       #9227465
# print('Количество вызовов:',c)                  #29_860_703
# print('Время:',time.time() - start_time)        #4.001256942749023

import math

#Упражнение 1
class Circle:
    def p(self,r):
        return 2 * r * 3.14
    def s(self,r):
        return 3.14*(r**2)


c = Circle()

# c.radius = 5
# print(c.p(c.radius))
# print(c.s(c.radius))

import datetime

#Упражнение №2
class Person():
    name = 'Человек'
    citizenship = 'Россия'
    birthdate = '1984-09-21'

    def age(self):
        print('Год рождения:',self.birthdate[:4])
        return datetime.date.today().year-int(self.birthdate[:4])

p = Person()
print(p.age())




def f(n):
    if n in f.__dict__: #если вычисляли ранее - результат
        return f.__dict__[n]
    else: #иначе - вычисляем n-ное число Фибоначчи
        if n == 0:
            f.__dict__[n] = 0
            return 0
        if n == 1:
            f.__dict__[n] = 1
            return 1
        else: # Рекурсивный вызов функции
            res = f(n-1) + f(n-2)
            f.__dict__[n] = res
            return res