class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def birth(self):
        self.age += 1


class Student(Person):
    def get_exam(self):
        try:
            return self.exam
        except AttributeError:
            return 0

    def set_exam(self, exam):
        self.exam = exam


pers1 = Person('Narek')
print(pers1.name)
print(pers1.age)
pers1.birth()
print(pers1.age)

stud = Student('Ass', 24)
print(stud.get_exam())
stud.set_exam('За супружеский долг - 2')
print(stud.get_exam())
stud.birth()
print('Пересдача, когда тебе будет', stud.age)
