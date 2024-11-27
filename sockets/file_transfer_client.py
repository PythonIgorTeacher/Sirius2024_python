import socket
s = socket.socket()
ip = "localhost"
port = 10_000
s.connect((ip, port))

filename = input('Введите имя файла для передачи: ')
#отправляем имя файла
s.send(bytes(filename, encoding='utf-8'))
#открываем файл в режиме побайтового чтения:
f = open(filename, 'rb')
#читаем первую строку:
line = f.read(1024)
while line: #отправялем остатки файла построчно
    s.send(line)
    line = f.read(1024)
f.close()
s.close()
print('Файл отправлен')



import socket
import threading
import os

class Buffer:
    def __init__(self,s):
        '''Buffer a pre-created socket.
        '''
        self.sock = s
        self.buffer = b''

    def get_bytes(self,n):
        '''Read exactly n bytes from the buffered socket.
           Return remaining buffer if <n bytes remain and socket closes.
        '''
        while len(self.buffer) < n:
            data = self.sock.recv(1024)
            if not data:
                data = self.buffer
                self.buffer = b''
                return data
            self.buffer += data
        # split off the message bytes from the buffer.
        data,self.buffer = self.buffer[:n],self.buffer[n:]
        return data

    def put_bytes(self,data):
        self.sock.sendall(data)

    def get_utf8(self):
        '''Read a null-terminated UTF8 data string and decode it.
           Return an empty string if the socket closes before receiving a null.
        '''
        while b'\x00' not in self.buffer:
            data = self.sock.recv(1024)
            if not data:
                return ''
            self.buffer += data
        # split off the string from the buffer.
        data,_,self.buffer = self.buffer.partition(b'\x00')
        return data.decode()


HOST = '127.0.0.1'
PORT = 2345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

with s:
    sbuf = Buffer(s)
    files = 'Достоевский.txt picture.jpeg'#input('Enter file(s) to send: ')
    files_to_send = files.split()

    for file_name in files_to_send:
        print(file_name)
        sbuf.sock.send(file_name.encode() + b'\x00')
        # sbuf.put_utf8(hash_type)
        # sbuf.put_utf8(file_name)

        file_size = os.path.getsize(file_name)
        sbuf.sock.send(str(file_size).encode() + b'\x00')

        with open(file_name, 'rb') as f:
            sbuf.sock.send(f.read())
        print('File Sent')