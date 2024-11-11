from threading import Thread,current_thread

flag = True
def spell():
    global flag
    while True:
        if flag == True and 'Thread-1' in current_thread().name:
            print(current_thread().name)
            flag = not flag #инвертируем флаг
        if flag == False and 'Thread-2' in current_thread().name:
            print(current_thread().name)
            flag = not flag #инвертируем флаг

t1 = Thread(target = spell)
t2 = Thread(target = spell)
t1.start()
t2.start()

def excercise_ping(url):
    ...
    if url:
        return True
    return False
class MyThread(Thread):
    def __init__(self, url):
        self.url = url
        print('сюда нужно поместить ваши argументы')
    def run(self):
        result = excercise_ping(self.url)
        print('это и есть ваша target-функция')