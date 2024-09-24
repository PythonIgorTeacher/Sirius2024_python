# class Example:
#     mode = 1
#     name = 'demo'
#
#
# a = Example()
# # print(a.__dict__)
# # print(id(a.mode))
# # print(id(Example.mode))
# # a.mode = 50
# #
# # print(id(a.mode))
# # print(a.__dict__)
# # b = Example()
# # print(b.mode)
# # b.mode = 50
# # print(id(b.mode))
# ###3 способа создания атрибутов:
# a.new = 'значение'
# setattr(a,'new_attr','value')
# a.__dict__['new_key'] = 'new_value'
# print(a.__dict__)
#
# # def new_method(a,b):
# #     return a*b
# # Example.method = new_method
# # c = Example()
# # print(c.method(5,5))
# ##Атрибута не существует
# print(getattr(Example, 'privet', 'Ошибка, атрибута не сущетсвет'))
# print(getattr(Example, 'mode', None))
#
# a.useless = None
# print(a.__dict__)
# del a.useless
# print(a.__dict__)
# delattr(a,'new_key')
# print(a.__dict__)
# delattr(a,'new_key')

# class Books:
#     '''Содержит список любимых книг'''
#     #favorites = []
#     def __init__(self,*args):
#         print('Вызван метод __init__')
#         l = list(args)
#         self.name = l.pop(0)
#         self.favorites = l
#
#
# tolya = Books('Толя')
# print(tolya.__dict__)
# # tolya.favorites.append('Айзек Азимов - Я, робот')
# # tolya.favorites.append('Анджей Сапковский - Ведьмак')
# print(tolya.__dict__)
#
# anya = Books('Аня')
# print('Книги Ани:',anya.favorites)

# class Person:
#     def __init__(self,name, money):
#         self._name = name         #protected - Защищенный
#         self.__money = money      #private - приватный
#
#     def show_money(self): #Метод - геттер
#         return f'Баланс аккаунта: {self.__money}'
#
#     def change_balance(self,delta): #Метод-сеттер
#         self.__money += delta


# new = Person('Иван Иванович', 100_000)
#
# # #Защищенный
# # # print(new.money)
# # print(new._name)
# # new._name = 'новый чел'
# # print(new._name)
#
# print(new.show_money())
# new.change_balance(-20_000)
# print(new.show_money())
# new.money ='сто тысяч рублей'


##Упражнение №1. Счетчик экземпляров
class Example:
    __instance_count = 0   #счетчик экземпляров на уровне Класса

    def __init__(self):
        Example.__instance_count += 1
        self.__serial_number = Example.__instance_count

    def current_instance_number(self):
        return 'Мой порядковый номер: '+ str(self.__serial_number)

    def show_total_instance_amount(self):#общее кол-во экземпляров
        return 'Общее количество объектов: '+str(Example.__instance_count)


a = Example()

b = Example()
c = Example()
Example.instance_count = 0
d = Example()
print(d.current_instance_number())
print(a.current_instance_number())
print(c.current_instance_number())
print(c.show_total_instance_amount())


##Решение от Вадима Гутника
# class TaxPayer:
# def __init__(self, name, ITIN, balance):
# self.__name = name
# self.__ITIN = ITIN
# self.__balance = balance
# def get_name(self):
# print(f"Имя налогоплательщика: {self.__name}")
# def set_name(self, name):
# self.__name = name
# def get_ITIN(self):
# print(f"ИНН налогоплательщика: {self.__ITIN}")
# def set_ITIN(self, ITIN):
# self.__ITIN = ITIN
# def get_balance(self):
# print(f"Баланс налогоплательщика: {self.__balance}")
# def set_balance(self, balance):
# self.__balance = balance