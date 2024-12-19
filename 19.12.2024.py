# #1
# phone = input()
# if (phone[:2] =='+7') and (len(phone) == 12) and (phone[2:].isdigit()==True):
#     print(True)
# else:
#     print(False)
# #2
# A,B,C = map(int,input().split())
# n = 0 #сколько бутылок куплено
#
# while A >= B:
#     bottles = A // B
#     n += bottles #Мы купили столько бутылок, имея А рублей по цене В
#     #A % B - Сдача после покупки
#     A = A % B + bottles * C #мы сдали A//B бутылок по цене C рублей
# print(n)

# ##3
# x = input()
# if x.isdigit() and 0 <= int(x) <= 100:
#      x = int(x) #преобразуем тип данных
#      if x <=30: print(2)
#      if 31 <= x <= 60: print(3)
#      if 61 <= x <= 80: print(4)
#      if x>80: print(5)
# else:
#     print('Недопустимое значение')
#
#
#
#
# try:
#      x = int(input()) #преобразуем тип данных
#      if not 0<=x<=100:
#          raise ValueError
#      if x <=30: print(2)
#      if 31 <= x <= 60: print(3)
#      if 61 <= x <= 80: print(4)
#      if x>80: print(5)
# except:
#     print('Недопустимое значение')
###4
s = input().lower()#текст входной
d = dict() #словарь для букв
for bukva in s:
    if bukva.isalpha(): #это символ-буква, не пробел, не запятая и т.д.
        if bukva in d: #смотрим в ключах словаря - была ли ранее буква
            d[bukva] += 1 #увеличиваем счетчик
        else: #такой буквы раньше не видели
            d[bukva] = 1 #при первой встрече -добавляем ключ bukva и значение 1
#Справка:
# print(d.keys()) #только ключи
# print(d.values())#Только значения
# print(d.items()) #пары (ключ, значение)
print(dict(sorted(d.items())))