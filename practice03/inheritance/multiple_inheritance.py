#1
class Father:
    def skills(self):
        print("Father: Driving")


class Mother:
    def skills(self):
        print("Mother: Cooking")


class Child(Father, Mother):
    pass


c = Child()
c.skills()   # Calls Father’s method (MRO)

#2
class Teacher:
    def teach(self):
        print("Teaching")


class Singer:
    def sing(self):
        print("Singing")


class Person(Teacher, Singer):
    pass


p = Person()
p.teach()
p.sing()

#3
class A:
    def show(self):
        print("Class A")


class B:
    def show(self):
        print("Class B")


class C(A, B):
    pass


obj = C()
obj.show()   # A is called first

#4
class A:
    def show(self):
        print("A")


class B:
    def show(self):
        print("B")


class C(A, B):
    def show(self):
        super().show()
        print("C")


c = C()
c.show()

#5
class Engine:
    def __init__(self):
        print("Engine ready")


class Wheels:
    def __init__(self):
        print("Wheels ready")


class Car(Engine, Wheels):
    def __init__(self):
        super().__init__()
        print("Car ready")


car = Car()