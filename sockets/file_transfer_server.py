# # import socket
# # s = socket.socket()
# # ip = "localhost"
# # port = 10_000
# # s.bind((ip, port))
# # s.listen(1)
# # while True:
# #     conn, addr = s.accept()
# #     print('Подключен:', addr)
# #     filename = (conn.recv(1024)).decode ('UTF-8')
# #     # открываем файл в режиме байтовой записи
# #     f = open( 'recieved_'+filename,'wb')
# #     while True: #записываем содержимое файла
# #         byte_line = conn.recv(1024)
# #         # пишем байтовые строки в файл на сервере
# #         f.write(byte_line)
# #         if not byte_line: #если все записано
# #             break
# #     f.close()
# #     conn.close()
# #     print('Файл получен')
# # s.close()
# #
# import socket
#
# s = socket.socket()
# ip = "localhost"
# port = 10_000
# s.bind((ip, port))
# s.listen(1)
# while True:
#     conn, addr = s.accept()
#     print('Подключен:', addr)
#     filename = (conn.recv(1024)).decode('UTF-8')
#     f = open('recieved_' + filename, 'wb')
#     while True:
#         byte_line = conn.recv(1024)
#         f.write(byte_line)
#         if not byte_line:
#             break
#     f.close()
#     conn.close()
#     print('Файл получен')
# s.close()




class Buffer:
    def __init__(self,s):
        self.sock = s
        self.buffer = b'' #буфер - байтовая строка

    def get_bytes(self,n): #Функция читающая ровно n байт из строки-буфера
        #если осталось меньше чем n Байт - вернет всё
        while len(self.buffer) < n:
            data = self.sock.recv(1024) #прочитали данные из сокета
            if not data: #если данных нет - чистим буфер
                data = self.buffer
                self.buffer = b''
                return data
            self.buffer += data#если данные есть -добабвляем их в буфер
        # вытаскиваем n байт из строки-буфера
        data,self.buffer = self.buffer[:n],self.buffer[n:]
        return data

    def put_bytes(self,data):
        self.sock.send(data) # отправка данных data

    def get_utf8(self):#читаем строку в кодироке UTF-8, окначивающуюся \00
        while b'\x00' not in self.buffer: #если в буфере еще нет \x00 -
            data = self.sock.recv(1024)#достаем часть данных
            if not data: #если данных нет совсем в сокете - вернем пустую строку
                return ''
            self.buffer += data #сохраняем данные в буфер
        # \x00 оказались в буфере - делим строку по символу \x00.
        #partiton - как split, Только для байтовых строк
        data,_,self.buffer = self.buffer.partition(b'\x00')
        return data.decode() #возвращаем декодированную строку

    def put_utf8(self,s): #отправка utf-8 строки
        if '\x00' in s:#если в данных оказался делитель |x00 -ошибка
            raise ValueError('string contains delimiter(null)')
        self.sock.sendall(s.encode() + b'\x00') #иначе - отправим все байты + разделитель


import socket
import os



HOST = ''
PORT = 2345

# If server and client run in same local directory,
# need a separate place to store the uploads.
try:
    os.mkdir('uploads')
except FileExistsError:
    pass

s = socket.socket()
s.bind((HOST, PORT))
s.listen(10)
print("Waiting for a connection.....")

while True:
    conn, addr = s.accept()
    print("Got a connection from ", addr)
    connbuf = Buffer(conn)

    while True:


        file_name = connbuf.get_utf8()
        if not file_name:
            break
        file_name = os.path.join('uploads',file_name)
        print('file name: ', file_name)

        file_size = int(connbuf.get_utf8())
        print('file size: ', file_size )

        with open(file_name, 'wb') as f:
            remaining = file_size
            while remaining:
                chunk_size = 4096 if remaining >= 4096 else remaining
                chunk = connbuf.get_bytes(chunk_size)
                if not chunk: break
                f.write(chunk)
                remaining -= len(chunk)
            if remaining:
                print('File incomplete.  Missing',remaining,'bytes.')
            else:
                print('File received successfully.')
    print('Connection closed.')
    conn.close()