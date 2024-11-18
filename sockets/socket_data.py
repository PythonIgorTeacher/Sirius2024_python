import socket
# создаем сокет:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#AF_INET для создания сокетов IPv4,
# SOCK_STREAM используется для указания сокета потока
#привязыаем сокет к порту, где он будет ожидать сообщения:
s.bind(('',10_000))
#Указываем, сколько соединений может принимать сокет:
s.listen(1)
print('Сервер работает')
while True:
    conn, addr = s.accept() #принимаем соединение
    print('Подключен:', addr)
    data = conn.recv(1024)  #принимаем данные по
    print(str(data))        # 1024 байта от клиента
    conn.send(data.upper()) #наш ответ клиенту
conn.close()                #закрываем соединение




