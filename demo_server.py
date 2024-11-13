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


#демо-чат одноканальный
import socket
#создаем сокет:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#AF_INET = сокет с протоколом IPv4
#SOCK_STREAM - потоковый сокет, TCP
s.bind(('localhost', 10_000)) #привязываем сокет к IP и  порту
#указываем количество соединений:
s.listen(1)
print('Сервер работает')
while True:
    conn, addr = s.accept() #принимаем соединениее conn - сокет клиента, addr- адрес
    print('Подключен: ', addr)

    input_message = conn.recv(1024) #принимаем данные по 1024 байта
    input_message = str(input_message.decode('utf-8'))
    print('client:', input_message) #тут нужно разнести функции в 2 потока - отдельно отправка, отдельно - прием
    output_message = input('server: ')
    if output_message == 'exit':
        break
    conn.send(bytes(output_message,encoding='utf-8')) #ответ клиенту

conn.close() #закрываем соединение
s.close()

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
#создаем сокет:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#AF_INET = сокет с протоколом IPv4
#SOCK_STREAM - потоковый сокет, TCP
s.bind(('localhost', 10_000)) #привязываем сокет к IP и  порту
#указываем количество соединений:
s.listen(1)
print('Сервер работает')
while True:
    conn, addr = s.accept() #принимаем соединениее conn - сокет клиента, addr- адрес
    print('Подклчен: ', addr)
    data = conn.recv(1024) #принимаем данные по 1024 байта
    data = str(data.decode('utf-8'))
    print(data)
    conn.send(bytes(data.upper(),encoding='utf-8')) #ответ клиенту

conn.close() #закрываем соединение
s.close()