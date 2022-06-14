class Woman():
    pass

class Person:
    i_have_father = True
    def __init__(self, name, age):
        self.name = name
        self.age  = age
    def say(self):
        print("my name is " + self.name + ", i have " + str(self.age) + " yars old")

alex = Person('alex', 19)
alex.say()


class Student(Person, Woman): # que constuctor estara heredando ?¿ se da precerencia a la primera clase para heredar su constructor
    notas = "estudiando"
    def mobing(self):
        print(self.name +  ' estoy ' + self.notas)

tania = Student('tania', 22)
tania.say()
tania.mobing()
print(tania.i_have_father)