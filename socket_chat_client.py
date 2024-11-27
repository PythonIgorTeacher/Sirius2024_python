#
# # #код клиента
# # import socket
# # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # s.connect(('localhost', 10_000))
# # s.send(bytes(f'Привет, сервер, меня зовут: {input("Введите ваше имя: ")}', encoding = 'utf-8'))
# # while True:
# #     data = s.recv(1024).decode('utf-8')
# #     output_message = input('client: ')
# #     if output_message == 'exit':
# #         break
# #     s.send(bytes(output_message, encoding='utf-8'))  # ответ клиенту
# # s.close()
# # print(data)
#
# from time import sleep
# from os.path import getsize
#



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





import socket
from threading import Thread
from datetime import datetime
from os.path import getsize

class Client:
    def __init__(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('localhost', 9_000))
        self.socket = s
        self.buffer = Buffer(self.socket)
        self.name = input('Выберите команду:\n1- выполнить вход(введите имя пользователя и пароль)\n2- регистрация ')
        self.buffer.sock.send(self.name.encode('utf-8') + b'\x00')  # отправили команду 1 или 2 серверу
        if self.name == '2': #пользователь хочет зарегистрироваться
            self.registration()
        else:
            authentication_flag = False #крутимся в цикле, пока правильно не войдем в аккаунт
            while not authentication_flag:
                authentication_flag = self.authenticate()

        self.type = self.socket.recv(1024).decode().split()[-1] #получили статус от сервера
        self.listener_flag = True
        self.listener = Thread(target = self.listen )
        self.listener.start()

        Thread(target = self.send_message).start()

    def registration(self):
        register_flag = True
        while True: #получение имени
            self.name = input('Введите имя: ')
            self.buffer.sock.send(self.name.encode('utf-8') + b'\x00')  # отправялем имя пользователя
            input_message = self.socket.recv(1024)  # ждем подтвержедния что имя хорошее
            input_message = str(input_message.decode('utf-8'))
            if input_message == '/ok':
                break
            else:
                print(input_message)
        while register_flag:
            new_password1 = input("Придумайте надежный пароль: ")
            new_password2 = input('Повторите пароль: ')
            if new_password1 == new_password2:
                register_flag = False
                self.password = new_password1 #сохранили пароль
                print('Пароль сохранен.')
                self.buffer.sock.send(self.password.encode('utf-8') + b'\x00')  # отправялем пароль
            else:
                print('Пароли не совпадают! Выполните повторный ввод.')

    def authenticate(self):
        #по логике в этом месте мы отправили серверу имя пользователя. Сервер должен проверить - есть ли это имя и правильно
        #ли введен пароль
        #ввод имени:
        while True: #получение имени
            self.name = input('Введите имя: ')
            self.buffer.sock.send(self.name.encode('utf-8') + b'\x00')  # отправялем имя пользователя
            input_message = self.socket.recv(1024)  # ждем подтвержедния что имя хорошее
            input_message = str(input_message.decode('utf-8'))
            if input_message == '/ok':
                break
            else:
                print(input_message)
        #ввод пароля:
        while True: #ввод пароля
            self.password = input("Введите пароль: ")
            if len(self.password) == 0:  # проверка пустого пароля
                print('Пароль не может быть пустым!')
                continue
            self.buffer.sock.send(self.password.encode('utf-8') + b'\x00')  # отправялем пароль
            input_message = self.socket.recv(1024)  # ждем подтвержедния что имя хорошее
            input_message = str(input_message.decode('utf-8'))
            if input_message == '/ok':
                break
            else:
                print(input_message)
        return True

    def listen(self):
        while self.listener_flag:
            try:
                input_message = self.socket.recv(1024) #принимаем данные по 1024 байта
                input_message = str(input_message.decode('utf-8'))
                print(input_message)
            except:
                pass
    def send_message(self):
        while True:
            output_message = input('>> ')
            if output_message == 'exit': #выход из программы
                self.socket.close()
                quit()
            #если отправлена команда /file_transfer
            if output_message.lower() == '/file_transfer' and self.type != "VIP":
                print("Вы не можете передавать файлы. Вы должны быть VIP-пользователем.")
                continue
            if output_message.lower() == '/file_transfer':
                filenames = input('Введите имя(имена) файла(ов) для отправки (через пробел): ')
                files_to_send = filenames.split() #Достоевский.txt picture.jpeg
                for file_name in files_to_send:
                    self.buffer.sock.send('/file_transfer'.encode('utf-8') + b'\x00')
                    print('Отправка файла: ', file_name)
                    # Отправляем 1 - имя файла, 2 - размер файла 3 - содержимое
                    self.buffer.sock.send(file_name.encode('utf-8') + b'\x00')
                    filesize = getsize(file_name)
                    self.buffer.sock.send(str(filesize).encode('utf-8') + b'\x00')
                    with open(file_name, 'rb') as f:
                        self.buffer.sock.send(f.read())
                    print(f'Файл {file_name} успешно отправлен')
                continue


            #отправка обычного сообщения
            self.buffer.sock.send(output_message.encode('utf-8') + b'\x00')


server = Client()

