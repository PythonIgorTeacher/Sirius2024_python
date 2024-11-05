# #Базовый функционал
# import multiprocessing as mp
#
# def func(x):
#     print(mp.current_process().name,mp.current_process().pid, x**2)
#     return x**2
#
# if __name__ == '__main__':
#     process = mp.Process(target = func, args = (2,)).start()
#     print('Готово')


# #Использование Pool
# import multiprocessing as mp
#
# def func(x):
#     print(mp.current_process().name,mp.current_process().pid, x**2)
#     return x**2
#
# if __name__ == '__main__':
#     with mp.Pool(5) as p:
#         result = p.map(func,[1,2,3,4,5,6])
#         print('Главный скрипт:', result)
# #1     process = mp.Process(target = func, args = (2,)).start()
# # 2     process = mp.Process(target = func, args = (2,)).start()
# # 3     process = mp.Process(target = func, args = (2,)).start()
# # 4     process = mp.Process(target = func, args = (2,)).start()
# # 5     process = mp.Process(target = func, args = (2,)).start()

# #Передача данных между процессами при помощи очередей
# import multiprocessing as mp
#
# def queue_put_func(q):
#     q.put([1,2,3])
#
# if __name__ == '__main__':
#     q = mp.Queue()
#     process = mp.Process(target = queue_put_func, args = (q,))
#     process.start()
#     print('В основной программе:',q.get())
#
#     print('Готово')

# #Передача данных между процессами при помощи конвееров - Pipes
# import multiprocessing as mp
# from time import sleep
# def get_data(connection):
#     l = [1,2,3]
#     sleep(5)
#     connection.send(l)
#     connection.close()
#
#
# if __name__ == '__main__':
#     parent_conn, child_conn = mp.Pipe() #родитель - получает, дочерний - передает
#     process = mp.Process(target = get_data, args = (child_conn,))
#     process.start()
#
#     print('В основной программе:', parent_conn.recv())
#     process.join()
#
#     print('Готово')


#Пример запуска мьютекса
import multiprocessing as mp
from time import sleep
def get_data(connection,lock):
    lock.acquire()
    l = [1,2,3]
    sleep(5)
    connection.send(l)
    connection.close()
    lock.release()

if __name__ == '__main__':
    lock = mp.Lock()
    parent_conn, child_conn = mp.Pipe() #родитель - получает, дочерний - передает
    process = mp.Process(target = get_data, args = (child_conn,lock))
    process.start()

    print('В основной программе:', parent_conn.recv())
    process.join()

    print('Готово')

#Переменные для подпрограмм
import multiprocessing as mp

def func(val, arr):
    val.value = 3.1415
    for i in range(len(arr)):
        arr[i] = -1 * arr[i]

if __name__ == '__main__':
    num = mp.Value('d',1.0)          #переменная вещественное число - 'd'
    array = mp.Array('i', range(10)) #массив целых чисел с типом - 'i'
    p = mp.Process(target=func, args=(num,array))
    p.start()
    p.join()
    print(num.value)
    print(array[:])
