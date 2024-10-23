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


# import threading
# import time
#
# def target_func(name, stop_thread):
#     while stop_thread():
#         print(f'Поток {name} работает')
#         time.sleep(1)
#     else:
#         print('Поток завершил работу')
#
# def user_interface(name):
#     global stop_thread
#     print(f'```````````````````{name} работает````````````````````',)
#     print(threading.current_thread().name[:8]) #t2
#
#     while t1.is_alive():
#         x = int(input('Введите значение: '))
#         if x ==0:
#             stop_thread = False
#
# stop_thread = True
# t1 = threading.Thread(target = target_func, args=('Первый поток', lambda :stop_thread,))
# t2 = threading.Thread(target = user_interface, args=('Второй поток',))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
#
# print('Конец работы')
#
#
#
# #https://www.geeksforgeeks.org/python-different-ways-to-kill-a-thread/

# x = 2
#
# import threading
# lock = threading.Lock()
# #первый поток
# lock.acquire()
# if x !=0:
#     print(10/x)
# lock.release()
# #второй поток
# ....
# x-=2
# ...


# import threading
# counter = 0
# lock = threading.Lock()
#
# def increment():
#     global counter
#     with lock: # lock.acquire()
#         for _ in range(10_000):
#             counter+=1
#     #lock.release()
#
# threads = [threading.Thread(target = increment) for _ in range(10)]
# [t.start() for t in threads]
# [t.join() for t in threads]
# print(counter)



# import threading
#
# lock = threading.Lock()
# f = open('threading.txt','w') #чтобы обнлуить файлик
# f.close()
#
#
# class Writer:
#     def __init__(self):
#         self.lock = threading.Lock()
#     def write(self, filename = 'threading.txt',value='' ):
#         with open(filename,'a') as f:
#             f.write(value+'\n')
#
# def thread_func(w:Writer):
#     thread_name = threading.current_thread().name
#     w.lock.acquire()
#     for i in range(10):
#         w.write(value=f'{thread_name}')
#     w.lock.release()
#
# w = Writer()
# threads = [threading.Thread(target = thread_func,args=(w, )) for _ in range(10)]
# [t.start() for t in threads]
# [t.join() for t in threads]



import threading

l = threading.Lock()
print('вызов 1')
l.acquire()             #1 -->0
try:
    print('Мои дела')
    int('буквы') #ОШИБКА! РЕЛИЗ НЕ СЛУЧИТСЯ
    l.release()
except:
    print('ошибка!')

print('вызов 2')
l.acquire()              #уже 0, ниже сделать нельзя, будет зависать
print('вызов 3')

lock = threading.Lock()
with lock:
    #наши действия
    pass
#самый безопасный вариант
try:
    #наши действия
    pass
except:
    pass
finally:
    lock.release()


#тормоз GIL:
#https://blog.marzeta.pl/deep-dive-into-pythons-gil-understanding-its-impact-on-multi-threading/