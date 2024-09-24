# class Circle:
#     def area(self, r):
#         return 3.14 * r**2
#     def perimeter(self, r):
#         return 2 * 3.14 * r
#
# c = Circle()
# print(c.perimeter(10))

'''

'''
# class Person:
#     name =''
#     citizenship = ''
#     birthdate = '2000-01-20'
#
#     def age(self):
#         year = int(self.birthdate[:4])
#         return current_year - year
#
# current_year = 2024
# p = Person()
#
# p.birthdate = '1984-01-20'
# print(p.__dict__)
# print(p.age())

# class Calculator:
#     def add(self,a,b):
#         return a + b
#     def sub(self,a,b):
#         return a - b
#     def mul(self,a,b):
#         return a * b
#     def pow(self,a,b):
#         return a ** b
#     def div(self,a,b):
#         if b == 0:
#             return 'err'
#         return a/b
#
# c = Calculator()
# print(c.mul(5,10))
# print(c.div(100,0))


# from random import randint, choice
# voice = {
#          'lion': 'roar',
#          'dog': 'bark',
#          'cat':'meow',
#          'bird': 'tweet',
#          'fox': ['roar','bark','meow','tweet']
#          }
#
# class Animal:
#     name = ''
#     def speak(self):
#         if self.name == 'fox':
#             return choice(voice[self.name])
#         return voice[self.name]
#
# a = Animal()
# a.name = 'fox'
# print(a.speak())
# print(a.speak())
# print(a.speak())

class Fraction:
    num = None
    den = None

    def show(self):
        if type(self.num) != int or not isinstance(self.den, int) or self.den == 0:
            return 'err'
        return f"{self.num}/{self.den}"
        #return str(self.num)+'/'+str(self.den)
    def simplify(self):
        if type(self.num) != int or not isinstance(self.den, int) or self.den == 0:
            return 'err'
        return self.num/self.den

f = Fraction()
f.num = 15#'числитель'
f.den = 10
print(f.simplify())