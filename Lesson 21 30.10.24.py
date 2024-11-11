# import threading
# semaphore = threading.Semaphore(1)
#
# x = 'перменная'
# semaphore.acquire()
# print("семафор занят")
# semaphore.release()
# semaphore.acquire()
# print(' увидим!')
#
#
# from threading import *
# from random import randint
# from time import sleep
#
# wifi_semaphore = Semaphore(4)
#
# def display():
#     wifi_semaphore.acquire()
#     print(f'пользователь {current_thread().name} подключился')
#     sleep(randint(2,5))
#     print(f'Отключение {current_thread().name} ')
#     wifi_semaphore.release()
#
#
#
#
# threads = [Thread(target=display) for _ in range(10)]
# [t.start() for t in threads]
# from queue import Queue
# from threading import Thread, current_thread, Lock
# from time import sleep, time
#
#
# toys = [('Снеговик',20,30), #0- имя, 1 - время изг. 2 - сколько штук
# ('Звезда', 45,11),
# ('Шарик', 5,100),
# ('Петушок', 27,10),
# ('Конь', 21,10),]
#
# q_lock = Lock()
# q = Queue()
# for toy in toys:
#     for _ in range(toy[2]):
#         q.put(toy[0:2])
#
#
# def create(q):
#     while not q.empty(): #пока очередь не пустая
#         print(f'{current_thread().name} хочет выбирать задачу')
#         q_lock.acquire()
#         print(f'{current_thread().name} выбирает задачу')
#         toy = q.get()
#         if 'Thread-1' not in current_thread().name and toy[1] >=25:
#             toys_list = [toy] #список тех, которые мы не можем изготовить
#             while not q.empty() and toy[1] >=25:
#                 toy = q.get() #берем следующую карточку задачи
#                 if toy[1] >=25:
#                     toys_list.append(toy)
#                     q.task_done()  #!!! тут была проблема. На каждый get нужно вызвать task_done
#                 else:
#                     break
#             else: #если мы не смогли выбрать задачу - остались только сложные
#                 for t in toys_list:  # складываем неподходящие карточки обратно
#                     q.put(t)  # перекладываем обратно в общую очередь
#                 q.task_done()  # !!! тут была проблема. На каждый get нужно вызвать task_done - эта строка для первого неудачного вызова get под строкой "поток выбирает задачу"
#                 q_lock.release()
#                 q.task_done()  # счетчик очереди отнимаем 1
#                 print(f'{current_thread().name} закончил работу, нет доступных задач')
#                 break
#             for t in toys_list: #складываем неподходящие карточки обратно
#                 q.put(t) #перекладываем обратно в общую очередь
#         q_lock.release()
#         print(f'{current_thread().name} закончил выбирать задачу')
#         print(f'{current_thread().name} изготавливает {toy[0]}')
#         sleep(toy[1]/100)
#         q.task_done() #счетчик очереди отнимаем 1
#     else:
#         print(f'{current_thread().name} закончил работу, нет доступных задач')
#
#
#
# master1 = Thread(target = create, args=(q,), daemon=True)
# master2 = Thread(target = create, args=(q,), daemon=True)
# master3 = Thread(target = create, args=(q,), daemon=True)
# # threads = [Thread(target= create, args = (q,), daemon=True) for _ in range(3)]
# # [t.start() for t in threads]
# start_time = time() #стартовое время работы
# master1.start()
# master2.start()
# master3.start()
#
# q.join()
# print(f'Заказ выполнен за {round(time() - start_time,3)}')

from threading import *
from time import sleep, time
from queue import Queue

s = Semaphore(3)

q = Queue()
toys = [('Снеговик',20,30), # 30
    ('Звезда', 45,11),
    ('Шарик', 5,100), # 100
    ('Петушок', 27,10),
    ('Конь', 21,10),]

for toy in toys:
    q.put(toy)

def fabric():
    while not q.empty():
        toy = q.get()
        s.acquire()
        if toy[1] < 25 and current_thread().name == "Thread-1 (fabric)":
            for _ in range(q.qsize()):
                check = q.get()
                if check[1] > 25:
                    q.put(toy)
                    toy = check
        print(f"Master {current_thread().name} is going to make the {toy[0]}")
        for item in range(toy[2]):
            if toy[1] > 25 and current_thread().name != "Thread-1 (fabric)":
                q.put(toy)
                break
            sleep(toy[1]//100)
            print(f"Master {current_thread().name} is finished {item+1} {toy[0]}")

        s.release()
        q.task_done()

t1 = Thread(target=fabric, daemon=True)
t2 = Thread(target=fabric, daemon=True)
t3 = Thread(target=fabric, daemon=True)
start = time()
t2.start()
sleep(0.1)
t3.start()
sleep(0.1)
t1.start()
t1.join(timeout=15)
t2.join(timeout=15)
t3.join(timeout=15)
print(f"Work is finished! It took {time()-start}  seconds!")
