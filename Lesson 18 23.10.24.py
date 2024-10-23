# from threading import Thread
# import time
#
# class MyCustomThread(Thread):
#     def __init__(self, *args):
#         super().__init__()
#         self.daemon = True     #тут могут быть ваши параметры потока
#         self.cycles = args[0]
#         self.values = args[1:]
#
#     def run(self):
#         print(self.values)
#         for i in range(self.cycles):
#             print('Шагов: ',i)
#             time.sleep(0.5)
# # t = threading.Thread(target = (), args=())
# t = MyCustomThread(5,4,3,2,1,0,0,0,0,0,0)
# t.start()
# print(t.is_alive())
# time.sleep(8)
# print(t.is_alive())



# ##Пример остановки потока через глобальную переменную
# import threading
# import time
#
# def target_func(name):
#     global flag
#     while flag == True:
#         print(f'Поток {name} работает')
#         time.sleep(1)
#     else:
#         print('Поток завершил работу')
#
# flag = True
# t = threading.Thread(target = target_func, args=('Имя потока - 1',))
# t.start()
#
# while True:
#     x = int(input('Введите значение: '))
#     if x ==0:
#         flag = False


import threading
import time

def target_func(name, stop_thread):
    while stop_thread():
        print(f'Поток {name} работает')
        time.sleep(1)
    else:
        print('Поток завершил работу')

def user_interface(name):
    global stop_thread
    print(f'```````````````````{name} работает````````````````````',)
    print(threading.current_thread().name) #t2

    while t1.is_alive():
        x = int(input('Введите значение: '))
        if x ==0:
            stop_thread = False

stop_thread = True
t1 = threading.Thread(target = target_func, args=('Первый поток', lambda :stop_thread,))
t2 = threading.Thread(target = user_interface, args=('Второй поток',))
t1.start()
t2.start()
t1.join()
t2.join()

print('Конец работы')



#https://www.geeksforgeeks.org/python-different-ways-to-kill-a-thread/