
# ##Пример отправки файла - сервер
# import socket
# s = socket.socket()
# ip = 'localhost'
# port = 9080
# s.bind((ip,port))
# s.listen(1)
# while True:
#     conn, addr = s.accept()
#     print('Подключен:',addr)
#     filename = (conn.recv(1024)).decode('utf-8') #получили имя файла в виде строки
#     f = open('received_'+filename, 'wb')
#     while True: #получаем файл построчно в виде байтовых строк
#         byte_line = conn.recv(1024)
#         f.write(byte_line) #записываем полученную информацию в файл
#         if not byte_line: #если всё передано
#             break
#     print('Файл:',filename,"получен")
#     f.close()
#     conn.close()
#     break
# s.close()




class Buffer:
    def __init__(self,sock):
        self.sock = sock  #ссылка на сокет
        self.buffer = b'' #наш буфер - байтовая строка
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
        data, sep, self.buffer = self.buffer.partition(b'\x00')
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


import socket
s = socket.socket()
ip = 'localhost'
port = 9080
s.bind((ip,port))
s.listen(1)
print('Сервер готов к работе и ждет подключений')
while True:
    conn, addr = s.accept()
    print('Подключен:',addr)
    connection_buffer = Buffer(conn)
    while True:
        #1 - имя файла, 2 - размер файла 3 - содержимое
        filename = connection_buffer.get_utf_8() #извлекаем декодированный текст - имя файла
        if not filename:
            break #что-то пошло не так, имя файла не пришло
        filesize = int(connection_buffer.get_utf_8())
        print(f'Файл: {filename}, размер: {filesize}')

        with open('получен_'+filename, 'wb') as f:
            remaining_size = filesize #столько байт осталось вытащить из соединения
            while remaining_size > 0:
                part_size = 1024 if remaining_size >= 1024 else remaining_size
                piece_of_file = connection_buffer.get_bytes(part_size)
                f.write(piece_of_file)
                remaining_size -= part_size
            print(f'Файл {filename} получен')
conn.close() #закрываем соединение клиента
s.close()