# import multiprocessing as mp
# import threading as tr
# import time
#
# def compute_sum(l,shared_dict):
#     result = sum(l)
#     shared_dict[mp.current_process().pid] = result
#
#
# if __name__ == '__main__':
#     manager = mp.Manager()
#     shared_dict = manager.dict() #создали общий словарь для процессов
#
#     nums = [i for i in range(10**8)]
#     n_cpu = mp.cpu_count() - 1
#     start_time = time.time()
#     for i in range(n_cpu):
#         print(i*len(nums)//n_cpu,(i+1)*len(nums)//n_cpu)
#
#     procesess = [mp.Process(target=compute_sum, args=(nums[i*len(nums)//n_cpu:(i+1)*len(nums)//n_cpu],shared_dict)) for i in range(n_cpu)]
#     [p.start() for p in procesess]
#     [p.join() for p in procesess]
#     print(sum(shared_dict.values()))
#
#     print(f'Процессы завершили работу. Время: {time.time()-start_time}') #2.77
#
#     start_time = time.time()
#     # for i in range(n_cpu):
#     #     print(i*len(nums)//n_cpu,(i+1)*len(nums)//n_cpu)
#     d = dict()
#     threads = [tr.Thread(target=compute_sum, args=(nums[i * len(nums) // n_cpu:(i + 1) * len(nums) // n_cpu], d)) for i
#                  in range(n_cpu)]
#     [t.start() for t in threads]
#     [t.join() for t in threads]
#     print(f'Потоки завершили работу. Время: {time.time() - start_time}')  # 2.77

##Упражнение №3
import multiprocessing as mp
from time import sleep, time


def child_process_function(q):
    count = 0
    while count != 5:
        name = q.get()
        print('Имя в дочернем процессе:', name)
        count+=1
    print('Выход из дочерней подпрограммы')


def parent_process_function(names_dict, q):
    while True:
        if len(names_dict['names'])>0:
                val = names_dict['names']
                name = val.pop(0)
                names_dict['names'] = val
                q.put(name)
                print('Добавлено имя в очередь:',name)
        sleep(2)
    print('Выход из РОДИТЕЛЬСКОЙ подпрограммы')

def watchdog(q):
    while True:
        last_q_size = q.qsize()
        sleep(12)
        print('Watchdog:', last_q_size)
        if q.qsize() == last_q_size:
            q.put('KILL PROCESS')


if __name__ == '__main__':
    manager = mp.Manager()
    names_dict = manager.dict()
    names_dict['names'] = [] #список имен пуст

    q = mp.Queue()
    parent_process = mp.Process(target=parent_process_function, args=(names_dict,q))
    child_process =  mp.Process(target=child_process_function, args=(q, ))
    wdog = mp.Process(target = watchdog, args=(q,), daemon = True)
    parent_process.start()
    child_process.start()
    wdog.start()
    count = 0
    while count < 5:
        name = input('Введите имя: ')
        val = names_dict['names']
        val.append(name)
        names_dict['names'] = val
        count +=1
    print('Цикл приема имен закончен')
    while True:
        sleep(12)
        message = q.get()
        print(message)
        if message == 'KILL PROCESS':
            parent_process.terminate()
            break
        else:
            q.put(message)
    child_process.join()
    parent_process.join()


#Не попадают имена в общий словарь!
#добавить Watchdog на родительский процесс
