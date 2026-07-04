class Person:
    def name(self):
        print("kamal")
    def age(self):
        print("19")
class Student(Person):
    def roll_no(self):
        print("22")
    def grade(self):
        print("A")
s1=Student()
s1.name()
s1.age()
s1.roll_no()
s1.grade()