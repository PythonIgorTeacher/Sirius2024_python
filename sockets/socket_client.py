import socket
# создаем сокет
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 10_000))#подключемся к серверному сокету
#'localhost' - указываем, что работаем на локальном компьютере
# отправляем сообщение:
s.send(bytes("сообщение для сервера", encoding = 'UTF-8'))
data = s.recv(1024)  # читаем ответ от серверного сокета
s.close()  # закрываем соединение
print(data.decode('utf-8'))


