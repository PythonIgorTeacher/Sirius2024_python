class Animal:
    def __init__(self,name,color):
        self.color = color
        self.name = name

    def __add__(self, other):
        return self.get_height() + other.get_height()
    def exist(self):
        print(f"{self.name} существует")

class Dog(Animal):
    def __init__(self,name, color, breed):
        super().__init__(name,color)
        self.breed = breed

    def bark(self):
        print(f"{self.name} породы {self.breed} лает")

a = Animal('Зверюга')
b = Animal('Птичка')
print(a+b)
d = Dog('Собака','Лайка')
d.exist()
d.bark()


import os
res = os.system('ping abracodabra.ru')
print('результат:')
print(res)