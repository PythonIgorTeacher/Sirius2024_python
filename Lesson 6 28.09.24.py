# class Fraction:
#     def __init__(self, num, den):
#         if type(num) != int or\
#             type(den) != int or\
#             den == 0:
#             raise ValueError('Числитель и знаменатель должны быть целыми числами. Знаменатель не должен быть равен нулю')
#         self.num = num
#         self.den = den
#
#     def show(self):
#         return f"{self.num}/{self.den}"
#     def simplify(self):
#         return self.num/self.den
#
#     def __add__(self, other):
#         if type(other) != type(self):
#             raise TypeError(f'Fraction can only add to Fraction. Not Fraction to {type(other)}')
#         common_divider = self.den * other.den
#         numerator = self.num * other.den + other.num * self.den
#         return Fraction(numerator, common_divider)
#     def __mul__(self, other):
#         if type(other) != type(self):
#             raise TypeError(f'Fraction can only multiply to Fraction. Not Fraction to {type(other)}')
#         return Fraction(self.num * other.num, self.den * other.den)
#     def __sub__(self, other):
#         if type(other) != type(self):
#             raise TypeError(f'Fraction can only sub to Fraction. Not Fraction to {type(other)}')
#         common_divider = self.den * other.den
#         numerator = self.num * other.den - other.num * self.den
#         return Fraction(numerator, common_divider)
#     def __truediv__(self, other):
#         if type(other) != type(self):
#             raise TypeError(f'Fraction can only truediv to Fraction. Not Fraction to {type(other)}')
#         return Fraction(self.num * other.den, self.den * other.num)
#     #__mul__, __sub__, __truediv__
#
# f1 = Fraction(3,7)
# f2 = Fraction(5,4)
# result = f1+f2
# print(result.show())
# print((f1*f2).show())
# print((f1-f2).show())
# print((f1/f2).show())
#

#
# import json
# class Car:
#     countOfCars = 0
#     def __init__(self, brand, color, maxSpeed, powerOfEngine, volumeOfEngine, typeOfBody, clearance, save=True):
#         self.__brand = brand
#         self.__color = color
#         self.__maxSpeed = maxSpeed
#         self.__powerOfEngine = powerOfEngine
#         self.__volumeOfEngine = volumeOfEngine
#         self.__typeOfBody = typeOfBody
#         self.__clearance = clearance
#         if save:
#             Car.add_car(self)
#         Car.countOfCars = Car.get_count_of_cars()
#
#     def go(self):
#         print("Машина едет.")
#
#     def break_(self):
#         print("Машина стоит")
#
#     @staticmethod
#     def print_stats(self):
#         print("Марка машины:", self.__brand)
#         print("Цвет машины:", self.__color)
#         print("Максимальная скорость машины:", self.__maxSpeed)
#         print("Мощность двигателя машины:", self.__powerOfEngine)
#         print("Объём двигателя машины:", self.__volumeOfEngine)
#         print("Тип кузова машины:", self.__typeOfBody)
#         print("Расстояние до земли у кузова машины:", self.__clearance)
#
#     # Получает полную информацию из JSON файла и возвращает её в виде словаря
#     @classmethod
#     def get_data(cls):
#         with open('cars.json') as f:
#             return json.load(f)
#
#     # Возвращает список с экземплярами всех машин
#     @classmethod
#     def get_cars(cls):
#         data = Car.get_data()
#         cars = []
#         for i in data:
#             if i == 'Count_Of_Cars':
#                 continue
#
#             cars.append(Car(
#                 data[i]['Brand'],
#                 data[i]['Color'],
#                 data[i]['Max_Speed'],
#                 data[i]['Power_Of_Engine'],
#                 data[i]['Volume_Of_Engine'],
#                 data[i]['Type_Of_Body'],
#                 data[i]['Clearance'],
#                 save=False
#             ))
#
#         return cars
#
#     # Выводит в консоль информацию о машинах в JSON файле
#     @classmethod
#     def print_cars(cls):
#         cars = Car.get_cars()
#         for i in cars:
#             Car.print_stats(i)
#             print('-' * 20)
#
#     # Добавляет новую машину в JSON файл
#     @classmethod
#     def add_car(cls, self):
#         car = {
#             "Brand": self.__brand,
#             "Color": self.__color,
#             "Max_Speed": self.__maxSpeed,
#             "Power_Of_Engine": self.__powerOfEngine,
#             "Volume_Of_Engine": self.__volumeOfEngine,
#             "Type_Of_Body": self.__typeOfBody,
#             "Clearance": self.__clearance
#         }
#         cars = Car.get_data()
#         cars['Count_Of_Cars'] += 1
#         cars[f"Car {cars['Count_Of_Cars']}"] = car
#         with open("cars.json", 'w') as f:
#             f.write(json.dumps(cars, indent=4,ensure_ascii=False,))
#
#     # Получает количество созданных объектов машин
#     @classmethod
#     def get_count_of_cars(cls):
#         with open('cars.json') as f:
#             return json.load(f)["Count_Of_Cars"]
#
#     # Удаляет машину из JSON файла. Нумерация машин в файле НЕ меняется
#     @classmethod
#     def delete_car(cls, car):
#         cars = Car.get_data()
#         cars["Count_Of_Cars"] -= 1
#         cars.pop(car)
#         with open('cars.json', 'w') as f:
#             f.write(json.dumps(cars, ensure_ascii=False))
#
#     # Удаляет все данные из JSON файла
#     @classmethod
#     def delete_data(cls):
#         with open('cars.json', 'w') as f:
#             f.write(json.dumps({"Count_Of_Cars": 0}))
#
#     # По вводам пользователя создаёт объект машины и возвращает его
#     @classmethod
#     def set_car(cls):
#         brand = input("Введите марку >> ")
#         color = input("Введите цвет >> ")
#         maxSpeed = int(input("Введите максимальную скорость >> "))
#         powerOfEngine = int(input("Введите мощность двигателя >> "))
#         volumeOfEngine = int(input("Введите объём двигателя >> "))
#         typeOfBody = input("Введите тип кузова >> ")
#         clearance = int(input("Введите расстояние от кузова до земли >> "))
#
#         return Car(brand, color, maxSpeed, powerOfEngine, volumeOfEngine, typeOfBody, clearance)
#
# Car.delete_data()
# c = Car('Honda','red',150, 150,1,'sedan',40,True)



# import math
# #
# # class Vector:
# #     def __init__(self, x, y):
# #         self.x = x
# #         self.y = y
# #
# #     def __add__(self, other):
# #         if isinstance(other, Vector):
# #             return Vector(self.x + other.x, self.y + other.y)
# #
# #     def __sub__(self, other):
# #         if isinstance(other, Vector):
# #             return Vector(self.x - other.x, self.y - other.y)
# #
# #     def __mul__(self, other):
# #         l1 = (self.x ** 2 + self.y**2) ** 0.5
# #         l2 = (other.x ** 2 + other.y ** 2) ** 0.5
# #         cos = (self.x * other.x + self.y * other.y)/ (l1*l2)
# #         return l1 * l2 * cos
# #     @staticmethod
# #     def length(vector):
# #         return (vector.x**2 + vector.y**2)**0.5
# #
# #
# #
# # v1 = Vector(5,5)
# # v2 = Vector(3,7)
# # v3 = v1-v2
# # print(v1*v2)
# # print(v3.x, v3.y )
# # print(v3.length(v3))
#
#
#
# class Employee:
#     def __init__(self,name):
#         if Employee.validate_name(name):
#             self.__name = name              #name - строка
#         else:
#             print('Валидация не сработала')
#         self.company = 'Рога И Копыта'
#     @property
#     def length_of_name(self):
#         return len(self.company)
#     @property
#     def name(self):
#         print('Работает геттер')
#         return self.__name
#     @name.setter
#     def name(self, new_name):
#         print('Работает сеттер')
#         if Employee.validate_name(new_name):
#             self.__name = new_name
#     @name.deleter
#     def name(self):
#         print('Работает делиттер')
#         self.__name = 'Не указано'
#
#     @staticmethod
#     def validate_name(name):
#         fio = name.split()
#         if not 2 <= len(fio) <= 3 or any([str(i) in name for i in range(10)]):
#             raise ValueError('Неправильный ввод ФИО')
#         else:
#             return True
#
#
# e = Employee('Карл Густав Юнг')
# print(e.name)
# e.name = 'Иаванов Иван Иванович'
# del e.name
#



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


new = Student('Филипп', 5.0)
l = [list(line.split()) for line in open('data.txt',encoding = 'utf-8')]
instances = []
for name in l:
    instances.append(Student(name[0],float(name[1])))

print(instances)

print(instances[0].student_name)
print(len(instances))