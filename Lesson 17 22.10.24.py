#Вопрос - GIL по времени проигрыш
#Вопрос - как остановить зависший поток.
#
# import threading
# import time
# from random import randint
#
# def sleepMe(name):
#     print(f"Поток {name} засыпает на 5 секунд")
#     time.sleep(randint(3,8))
#
#     if name == 5:
#         while True:
#             pass
#     print(f'Поток {name} проснулся')
#
#
# all_threads = []
# for i in range(10): #создаем 10 потокв в цикле
#                 #target - целевая функция
#     t = threading.Thread(target = sleepMe, args=(i,)) #создание потока
#     t.start()
#     all_threads.append(t)
#     #time.sleep(0.001) #время между запуском процессов
#
# for i in range(10):
#     all_threads[i].join(timeout=15) #python ждет завершения работы потоков, у которых вызван .join()
#
# print('Все потоки проснулись')


# import threading
# import time
#
# def thread_function(name,start,target):
#     for i in range(start,target+1,2):
#         time.sleep(0.3)
#         print(name,i)
#
# n = int(input('Введите число:\n'))
#
# daemon = True
# d = threading.Thread(target = thread_function, args=('T1 - ', 0, n), daemon = daemon)
# t2 = threading.Thread(target = thread_function, args=('T2 - ', 1, n), daemon = daemon)
# t1.start()
# time.sleep(0.01)
# t2.start()
# t1.join()
# t2.join()
# #
# print('готово')

#
from threading import Thread
import time

class MyCustomThread(Thread):
    def __init__(self, work_time):
        super().__init__()
        self.daemon = False     #тут могут быть ваши параметры потока
        self.work_time = work_time

    def run(self):
        start_time = time.time() #время начала работы
        while time.time() - start_time < self.work_time:
            print('Поток работает, осталось времени:',self.work_time - (time.time()-start_time) )
            time.sleep(0.5)

t = MyCustomThread(5)
t.start()

import sys
print(type(sys.version_info[1]) )
print(sys.argv[0])

