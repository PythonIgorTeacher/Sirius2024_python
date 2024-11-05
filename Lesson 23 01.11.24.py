# '''
# Attention! Сегодня мы решаем задачи с мудл-курса.
# Самостоятельная работа №6 - Многопоточность
# '''
#
#
from sys import setrecursionlimit
setrecursionlimit(5000)

def f(n):
    if n == 1:
        return 1
    else:
        return (n - 1) * f(n - 1)

def main():
    parts = input().split()
    a, b, c = map(int, parts)
    result = (f(a) + 2 * f(b)) / f(c)
    print(result)

if __name__ == "__main__":
    main()
