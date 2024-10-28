# #Упражнение
# import threading
# import random
#
# with open('file.txt','w') as f:
#     for i in range(1,31):
#         f.write(str(i)+'\n')
#
# used_numbers = []
# f = list(map(int,open('file.txt','r').readlines()))
# random.shuffle(f)
#
# lock = threading.Lock()
#
# def pick_number():
#     global used_numbers, f
#     lock.acquire()
#     x = random.choice(f)
#     while x in used_numbers:
#         x = random.choice(f)
#     used_numbers.append(x)
#     print(f"{threading.current_thread().name} число: {x}")
#     lock.release()
#
#
# threads = [threading.Thread(target = pick_number) for i in range(30)]
# [t.start() for t in threads]
# [t.join() for t in threads]
#
# print('Все потоки завершили работу')
#
#
#
# from threading import Thread, Lock
# from random import choice
#
# with open("file.txt", "w") as f:
#     f.write("\n".join([str(i) for i in range(1, 31)]))
#
# with open("file.txt", 'r') as f:
#     data = f.readlines()
#
#
# lock = Lock()
#
# def get_value(name):
#     global data
#     try:
#         lock.acquire()
#         value = choice(data)
#         data.remove(value)
#         print(f"Поток №{name} | Число №{value[:-1]}")
#     finally:
#         lock.release()
#
#
# threads = [Thread(target=get_value, args=(i,)) for i in range(1, 31)]
# [thread.start() for thread in threads]
# [thread.join() for thread in threads]
# print("Работа завершена!")
# import sys
# attribute = 10**10 + 5
# version = sys.version.split('.')
# if int(version[0]) >=3 and int(version[1]) >=11:
#     print(sys.getrefcount(attribute))
#     print(sys.getsizeof(attribute))
# else:
#     ...


def f(n):
    if n in (0,1): return n
    if n > 1:
        return 'value'
    else:
        return f(n-1) + f(n-2)

print(f(5))

a,b,c = map(int,input().split())


def f(a):
    if a == 1: return 1
    if a > 1: return (a-1) * f(a-1)