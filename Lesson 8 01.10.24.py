class Student():
    __student_list = []

    def __init__(self, student_name, average_score):
        self.__student_name = student_name
        self.__average_score = float(average_score)
        self.__student_list.append(student_name)

    def __del__(self):
        self.__student_list.remove(self.__student_name)

    def show_student_list(self):
        return self.__student_list

    def show_student_name(self):
        return self.__student_name

    def show_average(self):
        return self.__average_score

    def set_average_score(self, new_average_score):
        if type(new_average_score) == float and new_average_score >= 0 and new_average_score <= 5:
            self.__average_score = new_average_score
        else:
            print('Ошибка ввода данных')


with open('data.txt', encoding='utf-8') as f:
    l = [line.split() for line in f]
# l = [line.split() for line in open('data.txt', encoding='utf-8')]
instances = []
for name in l:
    instances.append(Student(name[0], float(name[1])))



for i, instance in enumerate(instances, 1):
    print(f"{i}. {instance.show_student_name()} {instance.show_average()}")

print(instances[0].show_student_list())
print(instances[0].show_average())

