import sys
from io import StringIO

# print('Версия пайтон:', sys.version)
# print('Путь к модулям:', sys.path)
# print('Список модулей:', sys.modules)

# print(type(sys.path))
# sys.path = []
# from pandas import *
# print(dir())

# print('Аргументы, попавшие в программу:')
# print(sys.argv)
# import sys
# sum = 0
# for i in range(1, len(sys.argv)):
#     sum += int(sys.argv[i])
#
# print(sum)

'''
sys является встроенным модулем, который предоставляет \n
доступ к переменным и функциям, которые используются \n
интерпретатором Python. 
Данные методы могут быть использованы для работы с \n
интерпретатором, строкой ввода-вывода, работой с \n
объектами внутри python-скриптов и многого другого

'''

# import sys
# #Чтение из строки ввода-вывода
# user_input = sys.stdin.readline()
# print(user_input)
#
# #печать в строку ввода вывода:
# sys.stdout.write('Ура, работает!\n')
# sys.stderr.write('Текст ошибки')

#
# from io import StringIO
# import sys
# tmp_stdout = sys.stdout #сохраняем ссылку на стандартную командную строку
#
# result = StringIO() #перехватываем информацию из консоли
# sys.stdout = result
#
# print('что-то печатаем')
# print('информация будет в переменной result')
#
# sys.stdout = tmp_stdout #вернули печать в консоль
#
# print('что мы перехватили:')
# print(result.getvalue())

# import sys, time
#
# def teleprint(text, delay=0.05):
#     for char in text:
#         sys.stdout.write(char)
#         time.sleep(delay)
# teleprint('Вы проснулись в темной пищере и ничего не видите',delay=0.1)


# import sys
# a = 'переменная'
# a += ' новое слово'
# a +='123'
# a = 'слово'
# print(sys.getrefcount(a))
# print(sys.getsizeof(a))
# l = [i for i in range(10**6)]
# g = (i for i in range(10**6))
# print(sys.getsizeof(l)/1024/1024)
# print(type(g))
# print(sys.getsizeof(g)/1024/1024)
# print(sys.maxsize)
# #9223372036854775807 = 2**63 -1
# #2147483647
# print(2**31 -1)

# import sys
# age = 20
# if age < 18:
#     sys.exit('Выход из программы. Возраст менее 18 лет')
# else:
#     print('продолжение работы')
#     quit('Выход!')
# from sys import setrecursionlimit
# from functools  import cache
# setrecursionlimit(10_000)
#
# @cache
# def f(n):
#     if n<=3: return n
#     return f(n-1) + f (n-2)
#
# print(f(10_000))


import sys
print(sys.getdefaultencoding())