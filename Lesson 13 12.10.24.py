# import sys
# sys.stdout.write(str(sys.argv[0])+'\n')
# sys.stdout.write(' '.join([str(val) for val in sys.argv[1:]]))
# sys.exit('\nЗавершение работы программы')

# import sys
# print(*sys.modules,sep='\n')


# import sys
# sys.path.append('./excercise')
# # sys.path=['./excercise'] #относительный импорт
# import my_module
# print(my_module.my_func('Значение'))
# print(type(sys.path))
#
#
# import excercise.my_module #Абсолютный импорт
# print(excercise.my_module.my_func('Значение'))

# import sys
# result = [i for i in range(5)]
# generator = (i for i in range(5))
#
# print(sys.getsizeof(result))    #89095160
# print(sys.getsizeof(generator)) #200
# for i in range(10):
#     print(next(generator))
# print(dir(result))
# print(dir(generator))


#

class Animal:
    name = 'Животное'
    @classmethod
    def change_animal_name(cls,value):
        cls.name = value

    def __init__(self,leg_count):
        self.__leg_count = leg_count
    @classmethod
    def get_school_name(cls):
        return cls.__school_name
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    # @property
    # def leg_count(self): #геттер
    #     return self.__leg_count
    # @leg_count.setter
    # def leg_count(self,new_value): #сеттер
    #     self.__leg_count = new_value
    #
    # @leg_count.deleter
    # def leg_count(self): #Делиттер
    #     self.__leg_count = None

    def __add__(self, other):
        return self.leg_count + other.leg_count


a = Animal(4)
b = Animal(8)
print(a+b)