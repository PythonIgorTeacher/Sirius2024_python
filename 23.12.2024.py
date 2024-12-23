# #задача №1.
# s, goal = input().split()
# word = list(s)
# flag = False #для отметки правильного ответа
# for i in range(len(word)-1):
#     for j in range(i+1,len(word)):
#         new_word = word.copy()
#         if i != j:
#             new_word[i],new_word[j] = new_word[j],new_word[i]
#             new_word = ''.join(new_word) #склеиваем список в строку
#             if new_word == goal:#чтобы сравнивать содержимое списка new_word и строку goal
#                 flag = True#нашли такую перестановку, которая получает правильный результат
# print(flag)


# ##2
# l = list(map(int,input().split())) #список чисел
# n = len(l) #длина списка
# for i in range(n): #перебираем длину неотсортированного списка, если i =0 - ничего не отсортировано, I = 1 значит самый большой элемент на своем месте и т.д.
#     flag = True #флаг для проверки факта перемещения
#     #j - индексы элементов в списке
#     for j in range(0,n-i-1): #-i чтобы уменьшить количество итераций с каждым шагом
#         if l[j] > l[j+1]: #если текущая цифра больше следующей
#             l[j],l[j+1] = l[j+1],l[j]  #меняем местами
#             #print(l)#для визуализации сортировки
#             flag = False
#     if flag: #если флаг не изменился за проход по цикул - останавливаем сортировку
#         break
# print(l)


# ##3
# d = {'row1':'zxcvbnm,./ZCVN<>?ячсмитьбю.ЯЧСМТБЮ,',
#      'row2':'asdfghjklp;\'ASDFGHJKL:\"фывапролджэФЫВАПРОЛДЖЭ',
#      'row3':'qwertyuiop[]WERTYUIOP{}\\|йцукенгшщзхъ\\ЙЦУКЕНГШЩЗХЪ/',
# }
# words = input().split()
# ok =[]
# for word in words: #перебираем слова
#     for row in d: #пербираем строки клавиатуры
#         if all(symbol in d[row] for symbol in word): #any - аналог All, проверяет что хотя бы одна истина
#             ok.append(word) #Добавляем слово к списку "правильных"
# print(sorted(ok))

#
# ##4
# s = input()
# ss = input()
# results = 0
# for i in range(len(s)): #i - индекс текущего места поиска
#     if s[i:i+len(ss)] == ss:
#         results +=1
# print(results)
#

##5
def recursive_caesar_cipher(s,k):

    #все буквы дублируются, ючтобы перескакивать в начало алфавита если мы шифруем крайние буквы
    encryption_word = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZабвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    if len(s) == 1:#последняя буква слова
        ind = encryption_word.index(s[0])#индекс символа, который мы кодируем
        return encryption_word[ind+k] #зашифрованная буква
    else: #если не последняя буква
        ind = encryption_word.index(s[0])#индекс символа, который мы кодируем
        return encryption_word[ind+k] + recursive_caesar_cipher(s[1:],k)
print(recursive_caesar_cipher('ЯХТА',4))


# for i in range(ord('А'), ord('Я')+1):
#     print(chr(i),end='')

