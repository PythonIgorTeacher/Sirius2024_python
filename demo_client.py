import socket
#создаем сокет:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#AF_INET = сокет с протоколом IPv4
#SOCK_STREAM - потоковый сокет, TCP
#привязываем сокет к IP и порту:
s.connect(('localhost', 10_000))
s.send(bytes('сообщение для сервера', encoding = 'utf-8'))
#получить данные 1024 байта:
data = s.recv(1024).decode('utf-8')
s.close() #закрываем соединение
print(data)

