
##код сервера
# import socket
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind(('localhost', 1000))
# s.listen(1)
# while True:
#     conn, addr = s.accept()
#     data = conn.recv(1024)
#     data = str(data.decode('cp1252'))
#     print('Получено:',data)
#     conn.send(bytes(data.upper(),encoding='cp1252'))
# conn.close()
# s.close()


##демо сокет
# import socket
# #создаем сокет:
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# #AF_INET = сокет с протоколом IPv4
# #SOCK_STREAM - потоковый сокет, TCP
# s.bind(('localhost', 10_000)) #привязываем сокет к IP и  порту
# #указываем количество соединений:
# s.listen(1)
# print('Сервер работает')
# while True:
#     conn, addr = s.accept() #принимаем соединениее conn - сокет клиента, addr- адрес
#     print('Подклчен: ', addr)
#     data = conn.recv(1024) #принимаем данные по 1024 байта
#     data = str(data.decode('utf-8'))
#     print(data)
#     conn.send(bytes(data.upper(),encoding='utf-8')) #ответ клиенту
#
# conn.close() #закрываем соединение
# s.close()


# #демо-чат одноканальный
# import socket
# #создаем сокет:
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# #AF_INET = сокет с протоколом IPv4
# #SOCK_STREAM - потоковый сокет, TCP
# s.bind(('localhost', 10_000)) #привязываем сокет к IP и  порту
# #указываем количество соединений:
# s.listen(1)
# print('Сервер работает')
# while True:
#     conn, addr = s.accept() #принимаем соединениее conn - сокет клиента, addr- адрес
#     print('Подключен: ', addr)
#
#     input_message = conn.recv(1024) #принимаем данные по 1024 байта
#     input_message = str(input_message.decode('utf-8'))
#     print('client:', input_message) #тут нужно разнести функции в 2 потока - отдельно отправка, отдельно - прием
#     output_message = input('server: ')
#     if output_message == 'exit':
#         break
#     conn.send(bytes(output_message,encoding='utf-8')) #ответ клиенту
#
# conn.close() #закрываем соединение
# s.close()

#
# import socket
# from threading import Thread
#
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET - IPv4 ; SOCK_STREAM - TCP ; SOCK_DGRAM - UDP
# server.bind(('', 9090))
# server.listen(10)
# print("Server is started.")
#
# connections = []
#
# def check_connection():
# conn, addr = server.accept()
# Thread(target=check_message, daemon=True).start()
# connections.append((conn, addr))
#
# def check_message(conn):
# data = conn.recv()
# send_message(conn, data)
#
# def send_message(conn, data): #except this conn
# for connection in connections:
# connection[0].send(data)
#
# watchdog = Thread(target=check_connection, daemon=True)
# watchdog.start()
#
# while True:
# input()
# break
#
# # closing all connections
# for connection in connections:
# connection[0].close()
# server.close()













import socket
from threading import Thread
from datetime import datetime
class Server:
    clients = []
    def __init__(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('localhost', 1000))
        s.listen(5) #количество одновременных подключений
        self.socket = s
        print('Сервер готов к работе, жду подключения')
        Thread(target=self.send_message).start()  # запускаем поток для отправки сообщений клиенту
        Thread(target=self.listen).start()

    def new_client(self):
        conn, addr = self.socket.accept()  # принимаем соединениее conn - сокет клиента, addr- адрес
        print('Подключен: ', addr)
        self.client_socket = conn
        input_message = self.client_socket.recv(1024)  # принимаем данные по 1024 байта
        input_message = str(input_message.decode('utf-8'))
        self.client_name = input_message


def listen(self):
        scripts = {
                   'привет':'Вас приветствует Socket-Server!',
                   'здравствуйте':'Вас приветствует Socket-Server!',
                   'пока': 'Всего доброго!',
                   'до свидания':  'Всего доброго!',
                   'время': f'На моих часах сейчас: [{str(datetime.now())[11:19]}]',
                    '/help': 'Для передачи файлов используйте команду /file_transfer',
                   }
        while True:
            input_message = self.client_socket.recv(1024) #принимаем данные по 1024 байта
            input_message = str(input_message.decode('utf-8'))
            for key in scripts.keys():
                if key in input_message.lower():
                    self.client_socket.send(bytes(scripts[key], encoding='utf-8'))  # ответ клиенту
            print('Сообщение входящее:', input_message)
            if input_message.lower() == '/file_transfer':
                print('Ожидается передача файла')
                filename = (self.client_socket.recv(1024)).decode('utf-8')  # получили имя файла в виде строки
                print('Имя файла:', filename)
                f = open('received_' + filename, 'wb')
                while True:  # получаем файл построчно в виде байтовых строк
                    byte_line = self.client_socket.recv(1024)
                    #print('получено|\t',byte_line.decode('utf-8'))
                    if '/end' in byte_line.decode('utf-8'):
                        print('передача файла завершена')
                        f.write(byte_line)  # записываем полученную информацию в файл
                        break

                print('Файл:', filename, "получен")
                f.close()
            print(f'[{str(datetime.now())[11:19]}] {self.client_name}:', input_message) #тут нужно разнести функции в 2 потока - отдельно отправка, отдельно - прием


    def send_message(self):
        while True:
            output_message = input('>> ')
            if output_message == 'exit': #выход из программы
                self.client_socket.close()
                self.socket.close()
                quit()
            self.client_socket.send(bytes(output_message, encoding='utf-8'))  # ответ клиенту

server = Server()

#доделать отправку файлов без костыля в виде /end
#доделать многопользовательский чат: Создаем класс Client и работаем с экземплярам