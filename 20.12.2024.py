# num_rows = int(input())
# if num_rows == 1:
#     print([[1]])
# elif num_rows == 2:
#     print([[1],[1,1]])
# elif num_rows >= 3:
#     l = [[1],[1,1]] #тут уже есть 0-я и первая строки, достраиваем остальные этажи
#     #перебираем строки:
#     for i in range(2,num_rows+1):#добавляем новые строки
#         line = []  # текущая строка - заготовка
#         #перебираем столбцы
#         for j in range(0,i+1):
#             if j == 0 or j == i:#если это крайняя левая или крайняя правая ячейка
#                 line.append(1)
#             else:
#                 line.append(l[i-1][j-1] + l[i-1][j])
#         l.append(line) #после напонления всех столбцов, добавляем строку к списку L
#
# for line in l:
#     print(*line,sep='\t')


#
# def roman_to_integer(s):
#     odd_romans = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900,
#                   'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#     result = 0
#     for key in odd_romans.keys():
#         while key in s:
#             result += odd_romans[key]
#             ind = s.find(key)  # индекс найденной цифры
#             s = s[:ind] + s[ind + len(key):]  # выкидываем использованную цифру
#     return result
# # print(roman_to_integer('MCMXCIV'))
# ##Недоделанная рекурсия:
# # from time import sleep
# # def recursive_roman_to_integer(s, result = 0):
# #
# #     print(s,result)
# #     sleep(3)
# #     odd_romans = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900,
# #                   'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
# #     if len(s) == 0:
# #         print('закончили')
# #         return result
# #     for key in odd_romans.keys():
# #         result += odd_romans[key] #Мы нашли цифру
# #         ind = s.find(key)  # индекс найденной цифры
# #         s = s[:ind] + s[ind + len(key):] #обрезаем строку
# #         return recursive_roman_to_integer(s,result)
# #     return result
# # print(recursive_roman_to_integer('MCMXCIV'))
#


total = 100_000
bull = 10_000  #a - количество быков
cow = 5_000    #b - коилчество коров
calf = 500     #c - количество телят
for a in range(0,101):
    for b in range(0, 101):
        for c in range(0, 101):
            if a+b+c == 100 and (bull*a + cow*b + calf * c) == total:
                print(a,b,c)