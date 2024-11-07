##Упражнение №4. Сортировка параллельно
import multiprocessing as mp
from random import shuffle

def sort_nums(l,q):
    unsorted = l
    for i in range(len(l)):
        flag = False
        for j in range(len(l)-i-1):
            if unsorted[j] > unsorted[j+1]:
                unsorted[j+1],unsorted[j] = unsorted[j], unsorted[j+1]
                flag= True
        if not flag:
            break
    q.put(unsorted)


def gather_all(q):
    print('Последний процесс')

    result = []
    while q.qsize()>0:
        result.extend(q.get())
    print(result)

if __name__ == '__main__':
    q = mp.Queue()

    nums = [i for i in range(10**3)] #генерируем список

    n_cpu = mp.cpu_count() - 2

    for i in range(n_cpu):
        print(i*len(nums)//n_cpu,(i+1)*len(nums)//n_cpu)

    procesess = [mp.Process(target=sort_nums, args=(nums[i*len(nums)//n_cpu:(i+1)*len(nums)//n_cpu],q)) for i in range(n_cpu)]
    [p.start() for p in procesess]
    [p.join() for p in procesess]
    last_process = mp.Process(target =gather_all, args=(q,))
    last_process.start()
    print(f'Процессы завершили работу.')

