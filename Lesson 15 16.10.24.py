# #Упражнение №5
# import os
#
# path = input()
#
# for path, dirs, files in os.walk(path):
#     print(f"Директории по пути {path}: ", dirs)
#     print(f"Файлы по пути {path}: ", files)
#     print()

# #Упражнение №6
# import os
# while True:
#     print('Выберите команду:\n1. Notepad\n2. date\n3. ping <address>\n4. regedit\n5. shutdown <time>\n6. Exit\n')
#     try:
#         num = int(input())
#         if not 1<=num<=6:
#             raise TypeError
#     except ValueError:
#         print('Допускается только ввод цифр')
#     except TypeError:
#         print('Неправильное значение. Вводите число от 1 до 6')
#     except:
#         print('Ошибка. Повторите ввод')
#
#     os.system('chcp 65001 > nul')
#     match num:
#         case 1:
#             os.system('notepad')
#         case 2:
#             os.system('date')
#         case 3:
#             print('Введите адрес узла:')
#             address = input()
#             os.system(f'ping {address}')
#         case 4:
#             os.system('regedit')
#         case 5:
#             while True:
#                 print('Введите время до отключения:')
#                 try:
#                     t = int(input())
#                     #os.system(f'shutdown -s -t {t}') #1200 секунд = 20 минут
#                     print(f'Отключение компьютера через {t} секунд')
#                     break
#                 except:
#                     print('Допускается только ввод цифр')
#         case 6:
#             print('выход')
#             quit()
#         case _:
#             print('пока не доделали')


# ##Упражнение №7
import sys
from io import StringIO
import os
address = input('Введите адрес узла: ')
tmp_stdout = sys.stdout #ссылка на стандартную консоль
result = StringIO()
sys.stdout = result
if os.path.exists('log.txt'):
    print('Файл открыт в режиме ДОЗАПИСИ')
    f = open('log.txt','a')
else:
    print('Файл открыт в режиме записи')
    f = open('log.txt','w')

os.system(f"ping {address}")
sys.stdout = tmp_stdout
for line in result.getvalue():
    print(line)
    f.write(line+'\n')
# import os
#
# address = input("Введите адрес пинга:")
# with open('log.txt', 'w', encoding='utf-8') as f:
#     f.write('')
#
# os.system(f"ping {address} > log.txt")




