#
# ##код сервера
# # import socket
# # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # s.bind(('localhost', 1000))
# # s.listen(1)
# # while True:
# #     conn, addr = s.accept()
# #     data = conn.recv(1024)
# #     data = str(data.decode('cp1252'))
# #     print('Получено:',data)
# #     conn.send(bytes(data.upper(),encoding='cp1252'))
# # conn.close()
# # s.close()
#
#
# ##демо сокет
# # import socket
# # #создаем сокет:
# # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # #AF_INET = сокет с протоколом IPv4
# # #SOCK_STREAM - потоковый сокет, TCP
# # s.bind(('localhost', 10_000)) #привязываем сокет к IP и  порту
# # #указываем количество соединений:
# # s.listen(1)
# # print('Сервер работает')
# # while True:
# #     conn, addr = s.accept() #принимаем соединениее conn - сокет клиента, addr- адрес
# #     print('Подклчен: ', addr)
# #     data = conn.recv(1024) #принимаем данные по 1024 байта
# #     data = str(data.decode('utf-8'))
# #     print(data)
# #     conn.send(bytes(data.upper(),encoding='utf-8')) #ответ клиенту
# #
# # conn.close() #закрываем соединение
# # s.close()
#
#
# # #демо-чат одноканальный
# # import socket
# # #создаем сокет:
# # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # #AF_INET = сокет с протоколом IPv4
# # #SOCK_STREAM - потоковый сокет, TCP
# # s.bind(('localhost', 10_000)) #привязываем сокет к IP и  порту
# # #указываем количество соединений:
# # s.listen(1)
# # print('Сервер работает')
# # while True:
# #     conn, addr = s.accept() #принимаем соединениее conn - сокет клиента, addr- адрес
# #     print('Подключен: ', addr)
# #
# #     input_message = conn.recv(1024) #принимаем данные по 1024 байта
# #     input_message = str(input_message.decode('utf-8'))
# #     print('client:', input_message) #тут нужно разнести функции в 2 потока - отдельно отправка, отдельно - прием
# #     output_message = input('server: ')
# #     if output_message == 'exit':
# #         break
# #     conn.send(bytes(output_message,encoding='utf-8')) #ответ клиенту
# #
# # conn.close() #закрываем соединение
# # s.close()
#
# #
# # import socket
# # from threading import Thread
# #
# # server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET - IPv4 ; SOCK_STREAM - TCP ; SOCK_DGRAM - UDP
# # server.bind(('', 9090))
# # server.listen(10)
# # print("Server is started.")
# #
# # connections = []
# #
# # def check_connection():
# # conn, addr = server.accept()
# # Thread(target=check_message, daemon=True).start()
# # connections.append((conn, addr))
# #
# # def check_message(conn):
# # data = conn.recv()
# # send_message(conn, data)
# #
# # def send_message(conn, data): #except this conn
# # for connection in connections:
# # connection[0].send(data)
# #
# # watchdog = Thread(target=check_connection, daemon=True)
# # watchdog.start()
# #
# # while True:
# # input()
# # break
# #
# # # closing all connections
# # for connection in connections:
# # connection[0].close()
# # server.close()
#
#
#
#
#
#
#
#
#
#
#
#


# 1. Сделать broadcast-message 'клиент {Name} подключился к серверу' OK

# 2. Сделать аутентификацию пользователей и разные типы аккаунтов (обычный, VIP)
# Vip -может отправлять файлы, обычный - нет.
# 3.  Логирование истории сообщений и имен файлов
class Buffer:
    def __init__(self, sock):
        self.sock = sock  # ссылка на сокет
        self.buffer = b''  # наш буфер - байтовая строка

    def get_bytes(self, n):  # функция извлекает n Байт из буфера
        while len(self.buffer) < n:  # если в нашем буфере меньше, чем n байт
            data = self.sock.recv(1024)  # запрашиваем из сокета 1024 байта
            if not data:
                data = self.buffer  # если в буфере не было n Байт, мы запросили их из сокета, и в сокете их не оказалось
                self.buffer = b''  # все данные что были в буфере - мы оптравляем в data, буфер - чистим
                return data
            self.buffer += data  # если данные есть - добавляем в буфер
        # если в буфере было >= n Байт
        data = self.buffer[:n]  # первые n Байт в переменную data
        self.buffer = self.buffer[n:]  # убираем первые n Байт из буфера
        return data

    def get_utf_8(self):  # получение данных в кодировке utf-8. \x00 - символ разделитель

        while b'\x00' not in self.buffer:  # пока в буефере не появился символ - разделитель
            # print(type(self.sock))
            data = self.sock.recv(1024)  # достаем из сокета 1024 байта
            if not data:
                return ''
            self.buffer += data

        # мы увидели \x00 - Конец файла в буфере - формируем файл целиком
        data, sep, self.buffer = self.buffer.partition(b'\x00')
        # в перемннную data - Упадет все что относится к нужному файлу
        # sep - символ разделитель \x00
        # остатки - кладем в буфер обратно
        return data.decode('utf-8')  # возвращаем декодированную строку

    def put_bytes(self, data):
        self.sock.send(data)

    def put_utf8(self, string):
        if b'\x00' in string:  # тут проверить!!!
            raise ValueError('Символ-разделитель \x00 есть в содержимом сообщения')

        self.sock.send(string.encode('utf-8') + b'\x00')


class Client:
    def __init__(self, addr, conn):
        self.addr = addr
        self.sock = conn
        self.buffer = Buffer(conn)
        self.client_name = None
        self.password = None
        self.status = None
    def __str__(self):
        return f'Client [{self.client_name}]' #<Client object at #12491425914adwagx 'main'>


##Сервер от 18.11.24
import socket
from threading import Thread
from datetime import datetime
from random import randint
import json

class Server:
    active_clients = []     #активные подключенные пользвователи
    user_names = []         #имена зарегистрированных пользователей из файла
    def __init__(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('localhost', 9_000))
        s.listen(5)  # количество одновременных подключений
        self.socket = s
        print('Сервер готов к работе, жду подключения')
        self.load_user_list() #вспоминаем пользователей при новом запуске программы
        print('Список известных имен пользователей:',Server.user_names)
        Thread(target=self.new_client).start()
        Thread(target=self.server_send_message).start()

    def load_user_list(self):
        try: #пробуем открыть файл. Если его нет - создаем
            with open('user_names.txt','r',encoding='utf-8') as f:
                Server.user_names = f.readline().replace(',','').split()
        except:
            f = open('user_names.txt','w',encoding='utf-8')
            f.close()
    # def load_user_data(self,username): #читаем Json юзера
    def dump_user_data(self,client): #запись данных о пользователе в файлы (имя - в один файл, порчие даннные  - в другой)
        with open('user_names.txt', 'a', encoding='utf-8') as f:
            f.write(client.client_name + ', ')
        with open('user_data.json','a') as f:
            keys = ['client_name', 'password','status']
            data_dict = {key: client.__dict__[key] for key in keys}
            json_object = json.dumps(data_dict)
            f.write(json_object)
            f.write('\n')

    def load_user_data(self,client:Client): #чтение данных о пользователе из Json файла
        name_index = Server.user_names.index(client.client_name) #узнали порядковый номер в списке имен
        with open('user_data.json','r') as f:
            i = 0
            for line in f:
                if i == name_index:
                    data = json.loads(line)
                    break
                i+=1
        for key in data: 
            client.__dict__[key] = data[key]

    def register(self, client:Client):
        # symbols = [chr(i) for i in range(ord('☃')-3,ord('☃')+20)] #старый механизм - когда добавляли символ в хвостик имени
        register_flag = True
        # РЕГИСТРИРУЕМ ПОЛЬЗОВАТЕЛЯ!
        while True:  # цикл проверки имени
            if register_flag:  # человек регистрируется
                client_name = client.buffer.get_utf_8()
                client.client_name = client_name
            if client.client_name in Server.user_names:
                client.sock.send('Выберите новое имя. Это имя уже занято'.encode('utf-8'))
                continue
            else:
                client.sock.send(b'/ok')
                client.client_name = client_name  # присваиваем имя
                password = client.buffer.get_utf_8()
                client.password = password  # тупо запомнили пароль при регистрации
                client.status = 'User'
                Server.user_names.append(client.client_name)  # записываем в список
                self.dump_user_data(client)
                # записать данные в файл
                break


    def authentication(self, user: Client):
        error_count = 0 #для подсчета ошибок
        # получаем имя
        while True:
            client_name = user.buffer.get_utf_8()
            if client_name in Server.user_names: #знаем такое имя:
                user.sock.send("/ok".encode())
                user.client_name =client_name
                self.load_user_data(user) #вытаскиваем из файла информацию о нашем пользователе
                break
            else:
                user.sock.send("Пользователь с таким аккаунтом не зарегистрирован. Повторите ввод имени".encode())
                error_count +=1
                if error_count == 5: #кикаем пользователя, если слишком много раз неправильно ввел данные
                    user.sock.send("Слишком много попыток входа. Соединение разорвано".encode())
                    user.sock.close()
                    Server.active_clients.remove(user)

        # получаем пароль
        while True:
            password = user.buffer.get_utf_8()
            if password != user.password:
                user.sock.send("Неправильный ввод пароля. Повторите ввод".encode())
                error_count +=1
                if error_count == 5: #кикаем пользователя, если слишком много раз неправильно ввел данные
                    user.sock.send("Слишком много попыток входа. Соединение разорвано".encode())
                    user.sock.close()
                    Server.active_clients.remove(user)
            else:
                user.sock.send("/ok".encode())
                break


        user.sock.send(f"Статус вашего аккаунта: {user.status}".encode())
        print(f'Приветствуем {Server.active_clients[-1].client_name} на сервере!')

    def new_client(self):
        #при подключении нового клиента - сообщение всем что "ИМЯ" подключился к серверу
        while True:
            conn, addr = self.socket.accept()  # принимаем соединениее conn - сокет клиента, addr- адрес
            print('Подключен: ', addr)
            #Клиент создается тут!!!
            Server.active_clients.append(Client(addr, conn))  # добавляем в список ссылку на подключение
            mode = int(Server.active_clients[-1].buffer.get_utf_8())  #Клиент подключается - выбор режима
            while mode not in (1,2): #если получили не цифры 1 или 2
                Server.active_clients[-1].sock.send('Выберите команду:\n1- выполнить вход(введите имя пользователя и пароль)\n2- регистрация '.encode('utf-8'))
                mode = int(Server.active_clients[-1].buffer.get_utf_8()) #ждем еще раз
            if mode == 1: #если получили 1 - вход
                self.authentication(Server.active_clients[-1])  # проверяем пароль
            else: #если получили 2 - регистрация
                self.register(Server.active_clients[-1])
            #после успешного входа на сервер или регистрации:
            self.broadcast_message(f'Приветствуем {Server.active_clients[-1].client_name} на сервере!')
            Thread(target=self.listen, args = (Server.active_clients[-1], )).start()


    def listen(self, client):
        scripts = {
            'привет': 'Вас приветствует Socket-Server!',
            'здравствуйте': 'Вас приветствует Socket-Server!',
            'пока': 'Всего доброго!',
            'до свидания': 'Всего доброго!',
            'время': f'На моих часах сейчас: [{str(datetime.now())[11:19]}]',
            '/help': 'Для передачи файлов используйте команду /file_transfer',
        }
        while True:
            input_message = client.buffer.get_utf_8()  #получаем сообщение
            print(f"[{str(datetime.now())[11:19]}][{client.client_name}][{client.status}]: {input_message}") #печатаем сообщение в терминале сервера
            if input_message.lower() == '/file_transfer':
                print('Ожидается передача файла')
                while True:
                    # 1 - имя файла, 2 - размер файла 3 - содержимое
                    filename = client.buffer.get_utf_8()  # извлекаем имя файла
                    if not filename:
                        break  # что-то пошло не так, имя файла не пришло
                    filesize = int(client.buffer.get_utf_8())
                    print(f'Получаю файл: {filename}, размер: {filesize}')
                    with open('получен_'+client.client_name+'_' + filename, 'wb') as f:
                        remaining_size = filesize  # столько байт осталось вытащить из соединения
                        while remaining_size > 0:
                            part_size = 1024 if remaining_size >= 1024 else remaining_size
                            piece_of_file = client.buffer.get_bytes(part_size)
                            f.write(piece_of_file)
                            remaining_size -= part_size
                        print(f'Файл {filename} получен')
                    break

            self.broadcast_message(f'[{str(datetime.now())[11:19]}][{client.client_name}][{client.status}]: {input_message}',client)

    def broadcast_message(self,message, sender = None):
        for client in Server.active_clients:
            if client != sender:
                client.sock.send(message.encode('utf-8'))

    def server_send_message(self): #это нужно доделать вам - функция для отправки сообщений с сервера
        while True:
            output_message = input('>> ')
            if output_message == 'exit':  # выход из программы
                for client in Server.active_clients:
                    client.sock.close()
                self.socket.close()
                quit()
            self.broadcast_message(output_message)

#что можно доделать:
#отправка файлов
#интерфейс с командами для сервера - например - изменить статус клиента /change_status client_name и тт.д.
#Шифрование данных пользователей
#Механизм смены пароля пользователем
#Выход из режима регистрации, выход из режима ввода имени/пароля
#Дописать генерацию Json Файла при первом запуске
server = Server()


# #Простой генератор паролей
# import secrets
# password = secrets.token_urlsafe(10)

#отправка ситсемных команд /file_Transfer  - не должна быть видна никому кроме сервера
#Доделка логирования:
# def log_message(self, data):
# if not os.path.exists("history.txt"):
# with open("history.txt", 'w') as f:
# f.truncate()
#
# with open("history.txt", 'a') as f:
# f.write(data)