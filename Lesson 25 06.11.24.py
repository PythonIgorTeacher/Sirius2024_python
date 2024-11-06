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


import multiprocessing as mp
from time import sleep




def child_process_function(q):
    count = 0
    while count != 5:
        name = q.get()
        print('Имя в дочернем процессе:', name)
        count+=1


def parent_process_function(names_dict, q):
    while True:
        print('Родительский процесс',names_dict)
        if len(names_dict['names'])>0:
                name = names_dict['names'].pop(0)
                q.put(name)
                print('Добавлено имя в очередь:',name)
        sleep(5)


if __name__ == '__main__':
    manager = mp.Manager()
    names_dict = manager.dict()
    names_dict['names'] = [] #список имен пуст
    q = mp.Queue()
    parent_process = mp.Process(target=parent_process_function, args=(names_dict,q))
    child_process =  mp.Process(target=child_process_function, args=(q, ))
    parent_process.start()
    child_process.start()
    count = 0
    while count < 5:
        name = input('Введите имя: ')
        names_dict['names'].append(name)
        count +=1

#Не попадают имена в общий словарь!
