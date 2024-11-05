# # import threading, time
# # parkRequests = 0
# # removeRequests = 0
# # parked = 0
# # removed = 0
# #
# # def parking_entry(): #поток, симулирующий поток автомобилей
# #     # тут создаётся несколько потоков для симуляции автомобилей
# #     while (True):
# #         time.sleep(1)
# #         incomingCar = threading.Thread(target=park_car)
# #         incomingCar.start()
# #         global parkRequests
# #         parkRequests = parkRequests + 1
# #         print(f"Запросов на парковку: {parkRequests}" )
# #
# #
# # def parking_exit():# Для потоков, симулирующих выезд автомобилей со стоянки
# #     while True:
# #         time.sleep(3)
# #         outgoingCar = threading.Thread(target=remove_car)
# #         outgoingCar.start()
# #         global removeRequests
# #         removeRequests = removeRequests + 1
# #         print(f"Запросов на выезд с парковки: {removeRequests}")
# #
# #
# #
# # def park_car(): #запарковать машину
# #     availbleParkings.acquire()
# #     global parkedLock
# #     parkedLock.acquire()
# #     global parked
# #     parked = parked + 1
# #     parkedLock.release()
# #     print(f"Фактически припарковано: {parked}" )
# # def remove_car(): #освободить машину
# #     availbleParkings.release()
# #     global removedLock
# #     removedLock.acquire()
# #     global removed
# #     removed = removed + 1
# #     removedLock.release()
# #     print("Фактически уехало с парковки: ",removed)
# #
# # parkedLock = threading.Lock()
# # removedLock = threading.Lock()
# # availbleParkings = threading.Semaphore(10) #всего 10 мест
# #
# # parking_entryThread = threading.Thread(target=parking_entry)
# # parking_exitThread = threading.Thread(target=parking_exit)
# # parking_entryThread.start()
# # parking_exitThread.start()
#
# # from threading import Semaphore, Thread
# # from time import sleep, time
# # from random import randint
# #
# # parkRequest = 0
# # removeRequest = 0
# #
# # parked = 0
# # removed = 0
# #
# # s = Semaphore(10)
# #
# # def park_car():
# #     global parked
# #     s.acquire()
# #     parked += 1
# #     print(f"Фактически припарковано = {parked}")
# #
# #
# # def remove_car():
# #     global removed
# #     removed += 1
# #     print(f"Фактически уехало = {removed}")
# #     s.release()
# #
# #
# # def parking_entry():
# #     global parkRequest
# #     while True:
# #         sleep(1)
# #         parkRequest += 1
# #         print(f"Запросов на парковку = {parkRequest}")
# #         #park_car()
# #         Thread(target=park_car).start()
# #
# # def parking_exit():
# #     global removeRequest
# #     while True:
# #         sleep(randint(2, 5))
# #         removeRequest += 1
# #         print(f"Запросов на выезд = {removeRequest}")
# #         Thread(target=remove_car).start()
# #
# #
# # parkcar = Thread(target=parking_entry, daemon=True)
# # removecar = Thread(target=parking_exit, daemon=True)
# # start = time()
# # parkcar.start()
# # removecar.start()
# # try:
# #     while True:
# #         pass
# # except KeyboardInterrupt:
# #     print(f"Парковка прикратила работу! Это заняло: {time()-start} секунд!")
# #     print(f"Сейчас на парковке {parked} машин.")
# #     print(f"За время работы симуляции уехало {removed} машин.")
# #     print(f"Запросов на заезд было {parkRequest}")
# #     print(f"Запросов на выезд было {removeRequest}")
#
# # #упражнение
# # from queue import Queue
# # from time import sleep
# # s = 'E A S * Y * Q U E * * * S T * * * I O * N * * *'.split()
# # q = Queue()
# # for symbol in s:
# #     if symbol.isalpha(): #or symbol !='*'
# #         q.put(symbol)
# #     else:
# #         print(q.get(symbol),end='')
# #     sleep(1)
#
#
# # #Задача про LiFo очередь
# # from queue import LifoQueue
# # s = input()
# # q = LifoQueue()
# # for symbol in s:
# #     q.put(symbol)
# # for symbol in s:
# #     print(q.get(),end='')
#
# # import threading
# # print('Ждем таймер')
# #
# # def timer_start():
# #     print('Таймер закончил работу!')
# #
# # timer = threading.Timer(5.6, timer_start)
# # timer.start()
#
#
# # import time
# # def compute_sum(N):
# #     return sum(range(1,N+1))
# #
# # start = time.time()
# # compute_sum(10**8)
# # print(time.time()- start) #4.21
#
#
# import time
# import threading
# result = [0,0,0,0]
# def compute_sum(i,start,end): #[1,N] --> [1,N//2]+[N//2+1, N]
#     result[i] = sum(range(start,end+1))
# N = 10**8
# start = time.time()
# t1 = threading.Thread(target=compute_sum,args=(0,0,N//4))
# t2 = threading.Thread(target=compute_sum,args=(1,N//4+1,N//2))
# t3 = threading.Thread(target=compute_sum,args=(2,N//2+1,3*N//4))
# t4 = threading.Thread(target=compute_sum,args=(3,3*N//4+1,N))
# t1.start()
# t2.start()
# t3.start()
# t4.start()
# t1.join()
# t2.join()
# t3.join()
# t4.join()
# total = sum(result)
# print(time.time()- start) #4.21
#
#
#
#
#
#
#
#
