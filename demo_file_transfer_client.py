
####Пример отправки файла - клиент
# import socket
# s = socket.socket()
# ip = 'localhost'
# port = 9080
# s.connect((ip,port))
# filename = input('Введите имя файла для отправки: ')
# #отправляем имя файла:
# s.send(filename.encode(encoding = 'utf-8'))
# f = open(filename, 'rb') #режим побайтового чтения
# line = f.read(1024)
# while line:
#     s.send(line)
#     line = f.read(1024)
# f.close()
# s.close()
# print('Файл отправлен')


class Buffer:
    def __init__(self,sock):
        self.sock = sock  #ссылка на сокет
        self.buffer = b'' #наш буфер - байтовая строка
    #\x00\x55\x44
    def get_bytes(self, n): #функция извлекает n Байт из буфера
        while len(self.buffer) < n:#если в нашем буфере меньше, чем n байт
            data = self.sock.recv(1024) #запрашиваем из сокета 1024 байта
            if not data:
                data = self.buffer #если в буфере не было n Байт, мы запросили их из сокета, и в сокете их не оказалось
                self.buffer = b''  #все данные что были в буфере - мы оптравляем в data, буфер - чистим
                return data
            self.buffer += data #если данные есть - добавляем в буфер
        #если в буфере было >= n Байт
        data = self.buffer[:n] #первые n Байт в переменную data
        self.buffer = self.buffer[n:] #убираем первые n Байт из буфера
        return data


    def get_utf_8(self): #получение данных в кодировке utf-8. \x00 - символ разделитель
        while b'\x00' not in self.buffer: #пока в буефере не появился символ - разделитель
            # print(type(self.sock))
            data = self.sock.recv(1024) #достаем из сокета 1024 байта
            if not data:
                 return ''
            self.buffer += data
        #мы увидели \x00 - Конец файла в буфере - формируем файл целиком
        data,sep,self.buffer = self.buffer.partition(b'\x00')
        #в перемннную data - Упадет все что относится к нужному файлу
        #sep - символ разделитель \x00
        #остатки - кладем в буфер обратно
        return data.decode('utf-8') #возвращаем декодированную строку

    def put_bytes(self, data):
        self.sock.send(data)

    def put_utf8(self,string):
        if b'\x00' in string:#тут проверить!!!
            raise ValueError('Символ-разделитель \x00 есть в содержимом сообщения')

        self.sock.send(string.encode('utf-8') + b'\x00')




from os.path import getsize
# from demo_file_transfer_server import Buffer
import socket
s = socket.socket()
ip = 'localhost'
port = 9080
s.connect((ip,port))
filenames = input('Введите имя(имена) файла(ов) для отправки (через пробел): ')

connection_buffer = Buffer(s)
files_to_send = 'Достоевский.txt picture.jpeg'.split()#filenames.split() #разбиваем имена файлов на список
for file_name in files_to_send:
    print('Отправка файла ',file_name)
    # 1 - имя файла, 2 - размер файла 3 - содержимое
    connection_buffer.sock.send(file_name.encode('utf-8')+b'\x00')
    filesize = getsize(file_name)
    connection_buffer.sock.send(str(filesize).encode('utf-8')+b'\x00')
    with open(file_name,'rb') as f:
        connection_buffer.sock.send(f.read())
    print(f'Файл {file_name} отправлен')

s.close()