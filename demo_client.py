
# #код клиента
# import socket
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(('localhost', 10_000))
# s.send(bytes(f'Привет, сервер, меня зовут: {input("Введите ваше имя: ")}', encoding = 'utf-8'))
# while True:
#     data = s.recv(1024).decode('utf-8')
#     output_message = input('client: ')
#     if output_message == 'exit':
#         break
#     s.send(bytes(output_message, encoding='utf-8'))  # ответ клиенту
# s.close()
# print(data)




import socket
from threading import Thread
from datetime import datetime
class Client:
    def __init__(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('localhost', 1000))
        self.socket = s
        self.name = "Клиент"#input('Введите имя: ')
        self.socket.send(self.name.encode())
        self.socket.send(f'Привет, меня зовут: {self.name}'.encode())
        Thread(target = self.listen ).start()
        Thread(target = self.send_message).start()
    def listen(self):
        while True:
            input_message = self.socket.recv(1024) #принимаем данные по 1024 байта
            input_message = str(input_message.decode('utf-8'))
            print(f'[{str(datetime.now())[11:19]}] server:', input_message)

    def send_message(self):
        while True:
            output_message = input('>> ')
            if output_message == 'exit': #выход из программы
                self.socket.close()
                quit()
            self.socket.send(output_message.encode(encoding='utf-8'))
            if output_message.lower() == '/file_transfer':
                filename = input('Введите имя файла для отправки: ')
                # отправляем имя файла:
                self.socket.send(filename.encode(encoding='utf-8'))
                f = open(filename, 'rb')  # режим побайтового чтения
                print('Отправляю файл')
                line = f.readline(1024)
                while line:
                    self.socket.send(line)
                    line = f.readline(1024)
                f.close()
                print('передача завершена')
                self.socket.send('/end'.encode(encoding='utf-8'))


            # self.socket.send(bytes(output_message, encoding='utf-8'))  # ответ клиенту

server = Client()



















