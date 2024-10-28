# import threading
#
# # l = threading.Lock()
# # print('1')
# # l.acquire()
# # print('2')
# # l.release()
# # print('3')
#
# class MyClass:
#     def __init__(self):
#         self.lock = threading.Lock()
#         self.counter = 0
#
#     def increment(self):
#         # self.lock.acquire() #вариант 1
#         self.counter +=1
#         # self.lock.release()
#
# m = MyClass()
# # m.lock.acquire() #вариант 2
# # m.increment()
# # m.lock.release()
#
# with m.lock:
#     print('работает')
#     #тут появится исключение
#
# m.lock.acquire()
# try:
#     print('работа')
# finally:
#     m.lock.release()


# from queue import Queue
# from queue import LifoQueue
# name = Queue()
# name.put('Владимир')
# name.put('Элона')
# name.put('Владислава')
# print(name.qsize())
# print(name.get())
# print(name.get())
# print(name.get())
#
# lifoname = LifoQueue()
# lifoname.put('Владимир')
# lifoname.put('Элона')
# lifoname.put('Владислава')
# print(lifoname.get())
# print(lifoname.get())
# print(lifoname.get())
#
#
# from queue import Queue
# name = Queue(maxsize = 3)
# name.put('Владимир')
# name.put('Элона')
# name.put('Владислава')
# # try:
# #     name.put('Хулиган',block=True,timeout=3)
# # except:
# #     pass
#
#
# if not name.full():
#     name.put('Хулиган',block=True,timeout=3)
# else:
#     print('Очередь занята!')
# print('Свободная ли очередь?', name.empty())
# print(name.qsize())
# print(name.get())
# print(name.get())
# print(name.get())
# print(dir(name))
# try:
#     print(name.get(timeout = 3))
# except:
#     print('Очередь пуста! Имен больше нет')
#


# from queue import Queue
# q1 = Queue()
#
# q1.put(1)
# q1.put(2)
# print(q1.get())
# q1.task_done()
# print(q1.get())
# q1.task_done()
#
# q1.join()
# print('Работа выполнена')



# from queue import Queue
# from threading import Thread
# from time import sleep
# from datetime import datetime
# from random import shuffle
# students = [(99,'Артем'),
#             (90, 'Нурбек'),
#             (88, 'Мадина'),
#             (76, 'Иван'),
#             (70,'Сергей'),
#             (65,'Тома'),
#             (50,'Михаил')]
# shuffle(students)
# q = Queue()
# for s in students:
#     q.put(s)
#
# def exam(q):
#     while not q.empty():
#         student = q.get() #(баллы[0], имя[1])
#         q.task_done()
#         print(f'Студент {student[1]} начал сдавать экзамен в {str(datetime.now())[11:19]}')
#         sleep((100-student[0])/5)
#         print(f'Студент {student[1]} закончил сдавать экзамен в {str(datetime.now())[11:19]}')
#
# professor1 = Thread(target = exam, args=(q,))
# professor2 = Thread(target = exam, args=(q,))
# professor1.start()
# professor2.start()
# q.join()
# print('Последний студент начал сдавать экзамен')
# professor1.join()
# professor2.join()
# print('Экзамен завершен')
#



from queue import Queue
from threading import Thread, Lock
import datetime
from time import sleep
q = Queue()

students = [(99,'Артем'),(90, 'Нурбек'),(88, 'Мадина'),(76, 'Иван'),(70,'Сергей'),(65,'Тома'),(50,'Михаил')]

[q.put(student) for student in students]

class StudentThread(Thread):
    teachers = 2
    def __init__(self, queue):
        super().__init__()
        self.queue = queue
        StudentThread.teachers -= 1
        if StudentThread.teachers <= -1:
            raise IndexError

    def run(self):
        q = self.queue
        while not q.empty():
            with Lock():
                get = q.get()
                print(f"{self.name} Студент {get[1]} начал экзамен в {datetime.datetime.now()}")
                sleep((100 - get[0]) / 5)
                print(f"Студент {get[1]} завершил экзамен в {datetime.datetime.ctime(datetime.datetime.now())}")

t1 = StudentThread(q)
t2 = StudentThread(q)
t1.start()
t2.start()
q.join()
print('последний ученик начал сдавать экзамен')


#https://collabedit.com/6ebgs