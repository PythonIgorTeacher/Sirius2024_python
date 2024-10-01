# '''
# Что нужно реализовать:
# 1) Функция отрисовки поля                                                draw_map
# 2) Функция, отвечающая за ход игрока                                     new_turn
# (получает номер клетки, проверяет не занята ли она, и фиксирует ход)
# 3) Функция проверки победы (или ничьей или окончания игры)               #check_win
# 4) Функция - начать сначала   команда RESTART                            #new_game
# 5) Функция - выход (Exit)
# Атрибуты:
# - Игровое поле - map - Одномерный список
# - Номер игрока - кто ходит. player = 0...1..2..3.4.5
# #Пример поля:
# _____________
# | 1 | 2 | 3 |
# _____________
# | 4 | 5 | 6 |
# _____________
# | 7 | 8 | 9 |
# _____________
# '''
# class TikTakToe:
#     def __init__(self):
#         self.map = [i for i in range(1,10)] #Карта мира
#         self.player = 0 #какой игрок ходит
#     def new_turn(self):
#         while True:
#             print(f'Ход игрока \'{"X" if self.player %2 ==0 else "O"}\'')
#             self.draw_map()
#             cell = input('Введите номер клетки в которую вы ставите метку: ')
#             if 'exit'  in cell.lower():
#                 quit()
#             elif 'restart'in cell.lower():
#                 self.restart()
#             try:
#                 cell = int(cell)
#                 if not 1 <= cell <= 9 or type(self.map[cell-1]) == str:
#                     raise ValueError
#             except:
#                 print('Введено неверное значение!')
#                 continue
#             self.map[cell - 1] = 'X' if self.player %2 ==0 else 'O' #запоминаем правильный ход
#
#             self.player +=1
#             break
#     def check_win(self): #проверка по столбцам и на ничью - отсутствует
#         if self.map[0] == self.map[1]==self.map[2] or\
#             self.map[3] == self.map[4] == self.map[5] or\
#             self.map[6] == self.map[7] == self.map[8] or\
#             self.map[0] == self.map[4] == self.map[8] or\
#             self.map[2] == self.map[4] == self.map[6]:
#             return f"Победил {'X' if (self.player+1) %2 ==0 else 'O'}"
#         else:
#             return False
#     def restart(self):
#         print('~~~~~~~~~~~~~~~~~~~~~Началась новая игра~~~~~~~~~~~~~~~~~~~~~')
#         self.map = [i for i in range(1,10)] #Карта мира
#         self.player = 0 #какой игрок ходит
#
#     def draw_map(self):
#         print(f"""_____________
# | {self.map[0]} | {self.map[1]} | {self.map[2]} |
# _____________
# | {self.map[3]} | {self.map[4]} | {self.map[5]} |
# _____________
# | {self.map[6]} | {self.map[7]} | {self.map[8]} |
# _____________
#                 """)
#
# game = TikTakToe()
# while True:
#     game.new_turn()
#     if game.check_win():  # проверка победы
#         print(game.check_win())
#         quit()



class Student():
    __student_list = []

    def __init__(self, student_name, average_score):
        self.student_name = student_name
        self.average_score = float(average_score)
        self.__student_list.append(student_name)

    def show_student_list(self):
        return self.__student_list

    def __del__(self):
        self.__student_list.remove(self.student_name)

f = open('data.txt','r',encoding='utf-8')
print(f.readlines())