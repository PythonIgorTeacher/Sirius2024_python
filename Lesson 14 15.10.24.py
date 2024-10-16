import os
# имя операционной
# print(os.name)
# #проверка доступа к файлу в разных режимах (регулируются флагами)
# print(os.access(r'C:\Users\Администратор\PycharmProjects\Sirius_2024\Lesson 13 12.10.24.py',
#                 os.X_OK))
#
# #R_OK
# #W_OK
# os.rmdir('New folder') #удаление папки
# os.mkdir('New folder') #создание папки
#
# #безопасное создание каталогов:
# os.makedirs('New folder', exist_ok=True)
# #переименование
# os.rename('Старое имя','Новое имя')

##получение текущей директории
# print(os.getcwd())
# print(os.listdir(path='New folder'))
# изменить директорю:
# os.chdir('New folder')
# os.chmod('New folder', mode = 5) #изменить права доступа к файлу
# os.chown() #поменять владельца
# print(os.getcwd())

# os.rmdir('New folder')
# os.removedirs('New folder')


# print(os.path.abspath('Lesson 14 15.10.24.py'))
# print(os.path.exists('file.txt'))
#
# #Работа с переменными среды ОС
# print(os.getenv('USERNAME'))
# print(os.environ)
# os.putenv('VARIABLE_NAME','VALUE')


# cmd = 'date'
# os.system('chcp 65001 > nul')
# os.system(cmd)
# os.system('notepad')

# print(os.utime('New folder/demo.txt', ))
#
# print(list(os.walk('students', topdown=True,
#         onerror=None,
#         followlinks=False)))

# #Упражнение №1.
# import os
#
# if os.name == 'nt':
#     print('Windows')
# elif os.name == 'posix':
#     print("Linux")
#
# print(os.getcwd())
# print(os.listdir())

# #упражнение 2
# import os
#
# path = input('Введите путь к каталогу: ')
# if os.path.exists(path):
#     print('Путь доступен')
#     items = os.listdir(path)
#     print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Список файлов:~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
#     for element in items:
#         if os.path.isfile(element):
#             print(element)
#     print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Список подкаталогов:~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
#     for element in items:
#         if os.path.isdir(element):
#             print(element)
#     print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Полный список:~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
#     for element in items:
#         print(element)
# else:
#     print('Путь не существует')
# import os
#
# path = input()
# print(os.path.exists(path))
# dirs = []
# files = []
# for elem in os.listdir():
#     if os.path.isfile(elem):
#         files.append(elem)
#     else:
#         dirs.append(elem)
#
# print(dirs)
# print(files)
# print(os.listdir())

# import os
#
# path = input()
#
# if os.access(path, mode=os.F_OK):
#     print("Файл существует")
# if os.access(path, mode=os.R_OK):
#     print("Файл можно читать")
# if os.access(path, mode=os.W_OK):
#     print("Файл можно редактировать")
# if os.access(path, mode=os.X_OK):
#     print("Файл можно запускать")
#
#
##Упражнение 4
import os
import time
path = r'C:\Users\Администратор\PycharmProjects\Sirius_2024\New folder\demo.txt'
file_info = os.stat(path)
print(file_info)
print(file_info.st_size, 'Байт')
print(oct(file_info.st_mode),'Режим доступа')
print(file_info.st_uid,'Владелец')
print(file_info.st_dev,'Устройство')
print(time.ctime(file_info.st_ctime),'Время создания')
print(time.ctime(file_info.st_mtime),'Время изменения')
print(time.ctime(file_info.st_atime),'Время открытия')