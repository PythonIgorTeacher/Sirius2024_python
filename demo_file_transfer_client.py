
####Пример отправки файла - клиент
import socket
s = socket.socket()
ip = 'localhost'
port = 9080
s.connect((ip,port))
filename = input('Введите имя файла для отправки: ')
#отправляем имя файла:
s.send(filename.encode(encoding = 'utf-8'))
f = open(filename, 'rb') #режим побайтового чтения
line = f.read(1024)
while line:
    s.send(line)
    line = f.read(1024)
f.close()
s.close()
print('Файл отправлен')