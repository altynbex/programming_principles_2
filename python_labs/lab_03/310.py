class Person():
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, gpa):
        super().__init__(name)
        self.gpa = gpa
    def display(self, name, gpa):
        print(f"Student: {name}, GPA: {gpa}")

name, gpa = map(str, input().split())
s1 = Student(name, gpa)
s1.display(name, gpa)