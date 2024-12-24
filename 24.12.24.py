"""Создайте абстрактный класс кресло с методами:
change_height, change_color, change_quality
и атрибутами:
height, price, color, quality
2. На  основе абстрактного класса реализуйте 2 вида кресел:
1) Компьютерное кресло
2) Кресло для чтения
"""

class InfoMixin:
    def __init__(self):
        raise PermissionError('Не создавайте экземпляры миксин классов')
    def show_info(self):
        try:#пробуем вызвать значения атрибутов
            return f"{self.price}, {self.color}, {self.quality}"
        except:#если атрбиутов не оказалось:
            return "Нет требуемых атрибутов"




from abc import ABC, abstractmethod, abstractproperty
class AbstractChair(ABC):
    @abstractmethod
    def change_height(self):
        pass
    @abstractmethod
    def change_color(self):
        pass
    @abstractmethod
    def change_quality(self):
        pass
    @abstractproperty
    def height(self):
        pass
    @abstractproperty
    def price(self):
        pass
    @abstractproperty
    def color(self):
        pass
    @abstractproperty
    def quality(self):
        pass

class ComputerChair(AbstractChair, InfoMixin):
    def __init__(self,height, color, price, quality = 100):
        self.__height = height
        self.__color = color
        self.__quality = quality
        self.__price = price

    def change_height(self, dy):
        self.__height += dy

    def change_color(self,new_color):
        self.__color = new_color

    def change_quality(self, difference):
        self.quality += difference

    @property
    def color(self):
        return self.__color
    @property
    def height(self):
        return self.__height
    @property
    def price(self):
        return self.__price
    @property
    def quality(self):
        return self.__quality
my_chair = ComputerChair(110,'Black',12000)
print(my_chair.quality)
print(my_chair.show_info())



'''1.Создайте класс ShoppingCart,
представляющий корзину для покупок.
Добавьте методы add_item, remove_item, calculate_total,
которые добавляют товар, убирают товар и вычисляют
общую стоимость товаров.
В качестве входных аргумента функции add_item, мы передаем объект класса
Item, обладающий атрибутами name, price
2. Добавьте методы геттер, сеттер, делиттер для списка товаров класса ShoppingCart
и добавьте декоратор property для метода calculate_total
(Возможно: перегрузка операторов)
3. Создайте дочерний класс LoggingShoppingCart, являющийся наследником класса ShoppingCart,
который логирует в файл Log.txt все действия, осуществляемые с экземпляром класса LoggingShoppingCart
(Возможна Многопоточность или многопроцессорность, либо sys/os, сокеты)
  '''


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}, {self.price}руб."


class ShoppingCart:
    def __init__(self):
        self.__item_list = []

    @property #создали метод-геттер
    def item_list(self): #Возвращает содержимое списка товаров
        print('Геттер')
        return self.__item_list

    @item_list.setter
    def item_list(self,item:Item): #"изменяет" значение прватного атрибута
        self.__item_list.append(item)
        print("сеттер")
        #self.__item_list.extend(other.items) #добавляем в этот список товаров товары из другого списка товаров

    @item_list.deleter #делитер - для удаления содержимого приватных атрибутов
    def item_list(self,item:Item):
        self.item_list.remove(item)

    # def add_item(self, item: Item):
    #     self.item_list.append(item)
    # def remove_item(self,item:Item):
    #     self.item_list.remove(item)

    @property
    def calculate_total(self):
        return sum([item.price for item in self.item_list])


class LoggingShoppingCart(ShoppingCart):
    def __init__(self):
        self.__item_list = []
        f = open('Log.txt','w',encoding='utf-8') #готовим файлик для логирования
        f.close()

    @property #создали метод-геттер
    def item_list(self): #Возвращает содержимое списка товаров
        f = open('Log.txt','a',encoding='utf-8')
        f.write(f'Вызван метод-геттер, содержимое списка: {[i.__str__() for i in self.__item_list]}\n')
        f.close()
        return self.__item_list

    @item_list.setter
    def item_list(self,item:Item): #"изменяет" значение прватного атрибута
        self.__item_list.append(item)
        f = open('Log.txt', 'a', encoding='utf-8')
        f.write(f'Вызван метод-сеттер, добавлено значение: {item.__str__()} содержимое списка: {[i.__str__() for i in self.__item_list]}\n')
        f.close()
        #self.__item_list.extend(other.items) #добавляем в этот список товаров товары из другого списка товаров

    @item_list.deleter #делитер - для удаления содержимого приватных атрибутов
    def item_list(self,item:Item):
        f = open('Log.txt','a',encoding='utf-8')
        f.write(f'Вызван метод-делиттер, удален объект: {item.__str__()}\n')
        f.close()
        self.item_list.remove(item)

    @property
    def calculate_total(self):
        price = sum([item.price for item in self.item_list])
        f = open('Log.txt','a',encoding='utf-8')
        f.write(f'Вызван метод calcuate_total, стоимость товаров в корзине: {price}\n')
        f.close()
        return price

banana = Item('Банан', 150)
milk = Item('Молоко',120)
sc = LoggingShoppingCart()
sc.item_list = banana #вызываем сеттер
sc.item_list = milk #вызываем сеттер
sc.item_list = banana #вызываем сеттер
print(sc.item_list,sep =', ') #вызываем геттер
print(sc.calculate_total)
# print(sc.calculate_total())
# print([id(item) for item in sc.item_list])
# banana.price = 100
# print(sc.calculate_total())
# print([id(item) for item in sc.item_list])
print(banana)