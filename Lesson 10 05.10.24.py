# import abc
# from abc import ABC, abstractmethod
#
# class Furniture(ABC):
#     size: int
#     brand: str
#     my_class_attribute = 0
#     @classmethod
#     @abstractmethod
#     def my_abstract_classmethod(cls, *args): pass
#
#
#     # @staticmethod
#     # @abstractmethod
#     # def my_abstract_staticmethod(*args): pass
#
#     @abstractmethod
#     def info(self): pass
#
#     @property
#     @abstractmethod
#     def value(self): pass
#     @value.setter
#     @abstractmethod
#     def value(self,new_value): pass
#
#     def exist(self):
#         print(f'{self.__class__.__name__} существует')
#
#
#
# class Table(Furniture):
#     counter = 0
#     def __new__(cls, *args, **kwargs):
#         o = object.__new__(cls)
#         del o.exist #деструктор не вызывается, Exist не видится классом Table
#         return o
#     def __init__(self, name, value=0):
#         Table.counter +=1
#         self.name = name
#         self.__value = value
#
#     @classmethod
#     def my_abstract_classmethod(cls,*args):
#         return cls.counter
#
#     @property
#     def value(self): return self.__value
#
#     @value.setter
#     def value(self, new_value):
#         self.__value = new_value
#
#     def info(self):
#         return f"Стол: {self.name}"
#
#
#
# new = Table('кухонный')
# new.exist()
# print(new.info())
# print(new.my_abstract_classmethod())


#https://refactoring.guru/ru/design-patterns/catalog


from abc import ABC, abstractmethod
class AbstractTable(ABC):
    @abstractmethod
    def has_legs(self): pass
    @abstractmethod
    def sit_on(self): pass
class AbstractChair(ABC):
    @abstractmethod
    def has_legs(self): pass
    @abstractmethod
    def sit_on(self): pass
class AbstractSofa(ABC):
    @abstractmethod
    def has_legs(self): pass
    @abstractmethod
    def sit_on(self): pass

class AbstractFurnitureFactory(ABC):
    @abstractmethod
    def create_table(self): pass
    @abstractmethod
    def create_chair(self): pass
    @abstractmethod
    def create_sofa(self): pass


class CardoardFurnitureFactory(AbstractFurnitureFactory):

    class CardboardTable(AbstractTable):
        def __init__(self,legs_count):
            self.legs_count = legs_count
        def has_legs(self):
            return self.legs_count > 0
        def sit_on(self):
            return f"Вы сели на {self.__class__.__name__}"
    class CardboardSofa(AbstractSofa):
        def __init__(self,legs_count):
            self.legs_count = legs_count
        def has_legs(self):
            return self.legs_count > 0
        def sit_on(self):
            return f"Вы сели на {self.__class__.__name__}"
    class CardboardChair(AbstractChair):
        def __init__(self,legs_count):
            self.legs_count = legs_count
        def has_legs(self):
            return self.legs_count > 0
        def sit_on(self):
            return f"Вы сели на {self.__class__.__name__}"


    def create_table(self, legs_count):
        table = CardoardFurnitureFactory.CardboardTable(legs_count)
        return table

    def create_chair(self,legs_count):
        chair = CardoardFurnitureFactory.CardboardChair(legs_count)
        return chair

    def create_sofa(self,legs_count):
        sofa = CardoardFurnitureFactory.CardboardSofa(legs_count)
        return sofa

factory = CardoardFurnitureFactory()
table = factory.create_table(3)
chair = factory.create_chair((4))
print(chair.sit_on())
