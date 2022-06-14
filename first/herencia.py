class Person:
    def __init__(self, name, age):
        self.name = name
        self.age  = age
    def say(self):
        print("my name is " + self.name + ", i have " + str(self.age) + " yars old")

alex = Person('alex', 19)
alex.say()

class Student(Person):
    pass

tania = Student('tania', 22)
tania.say()
