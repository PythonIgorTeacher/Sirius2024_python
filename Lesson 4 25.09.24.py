# # Решение от Вадима Гутника
# class TaxPayer:
#     def __init__(self, name, ITIN, balance):
#         self.__name = name
#         self.__ITIN = ITIN
#         self.__balance = balance
#
#     def get_name(self):
#         print(f"Имя налогоплательщика: {self.__name}")
#
#     def set_name(self, name):
#         self.__name = name
#
#     def get_ITIN(self):
#         print(f"ИНН налогоплательщика: {self.__ITIN}")
#
#     def set_ITIN(self, ITIN):
#         self.__ITIN = ITIN
#
#     def get_balance(self):
#         print(f"Баланс налогоплательщика: {self.__balance}")
#
#     def set_balance(self, balance):
#         self.__balance = balance
#
# ivan = TaxPayer('Иван', 123_456_789_123, 0)
# ivan.set_balance(-953.21)
# ivan.get_balance()
# print(ivan.__dict__)
# print(TaxPayer.__dict__)





# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def get_x(self):
#         return self.__x
#
#     def get_y(self):
#         return self.__y
#
#     def set_x(self, new_x):
#         self.__x = new_x
#
#     def set_y(self, new_y):
#         self.__y = new_y
#
#     def move(self, dx, dy):
#         self.set_x(self.__x + dx)
#         self.set_y(self.__y + dy)
#
#     def length(self, point):
#         x = self.get_x() - point.get_x()
#         y = self.get_y() - point.get_y()
#         dist = (x**2 +y**2) ** 0.5
#         return dist
#
# p1 = Point(0, 0)
# p2 = Point(3,4)
# print(p1.length(p2))


class Stack:
    def __init__(self):
        self.__items = []
    def push(self,value):
        #'''метод для добавления элемента в стек'''
        self.__items.append(value)
    def pop(self):
        if self.is_empty():
            return None
        return self.__items.pop(-1)

    def is_empty(self):
        return len(self.__items) == 0

s = Stack()
s.push(1)
s.push(5)
s.push(10)
print(s.pop()) #10
print(s.pop()) #5
print(s.pop()) #1


# class Deque:
#     def __init__(self):
#         self.__elems =[]
#
#     def push(self, elem):
#         self.__elems.append(elem)
#     def pop(self):
#         return self.__elems.pop(0)
#     def size(self):
#         return len(self.__elems)
#     def is_empty(self):
#         return True if len(self.__elems) == 0 else False
#         #return len(self.__elems) == 0
#     def peek(self):
#         return self.__elems[0]

'''
Что нужно реализовать:
1) Функция отрисовки поля                                                draw_map
2) Функция, отвечающая за ход игрока                                     new_turn
(получает номер клетки, проверяет не занята ли она, и фиксирует ход)     
3) Функция проверки победы (или ничьей или окончания игры)               #check_win
4) Функция - начать сначала   команда RESTART                            #new_game
5) Функция - выход (Exit)
Атрибуты:
- Игровое поле - map - Одномерный список
- Номер игрока - кто ходит. player = 0...1..2..3.4.5
#Пример поля:
_____________
| 1 | 2 | 3 |
_____________
| 4 | 5 | 6 |
_____________
| 7 | 8 | 9 |
_____________

'''

class TikTakToe:
    def __init__(self):
        self.map = [i for i in range(1,10)] #Карта мира
        self.player = 0 #какой игрок ходит
    def new_turn(self):
        while True:
            print(f'Ход игрока \'{"X" if self.player %2 ==0 else "O"}\'')
            self.draw_map()
            cell = input('Введите номер клетки в которую вы ставите метку: ')
            try:
                cell = int(cell)
                if not 1 <= cell <= 9 or type(self.map[cell-1]) == str:
                    raise ValueError
            except:
                print('Введено неверное значение!')
                continue
            self.map[cell - 1] = 'X' if self.player %2 ==0 else 'O' #запоминаем правильный ход

            self.player +=1
            break

    def draw_map(self):
        print(f"""_____________
| {self.map[0]} | {self.map[1]} | {self.map[2]} |
_____________
| {self.map[3]} | {self.map[4]} | {self.map[5]} |
_____________
| {self.map[6]} | {self.map[7]} | {self.map[8]} |
_____________
                """)


game = TikTakToe()
game.new_turn()
game.new_turn()
game.draw_map()