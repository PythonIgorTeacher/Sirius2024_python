class Student:
    __student_list = []

    def __init__(self, student_name, average_score):
        self.student_name = student_name
        self.average_score = average_score
        Student.__student_list.append(student_name)

    def show_student_list(self):
        return Student.__student_list

    def __del__(self):
        Student.__student_list.remove(self.student_name)

s = Student('Жаба',14)