
##Пример отправки файла - сервер
import socket
s = socket.socket()
ip = 'localhost'
port = 9080
s.bind((ip,port))
s.listen(1)
while True:
    conn, addr = s.accept()
    print('Подключен:',addr)
    filename = (conn.recv(1024)).decode('utf-8') #получили имя файла в виде строки
    f = open('received_'+filename, 'wb')
    while True: #получаем файл построчно в виде байтовых строк
        byte_line = conn.recv(1024)
        f.write(byte_line) #записываем полученную информацию в файл
        if not byte_line: #если всё передано
            break
    print('Файл:',filename,"получен")
    f.close()
    conn.close()
    break
s.close()


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