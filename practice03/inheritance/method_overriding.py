#1
class Animal:
    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):
    def speak(self):
        print("Dog barks")


a = Animal()
d = Dog()

a.speak()
d.speak()   # overridden method

#2
class Vehicle:
    def start(self):
        print("Vehicle is starting")


class Car(Vehicle):
    def start(self):
        super().start()
        print("Car engine is running")


car = Car()
car.start()

#3
class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no


s = Student("Alex", 10)
print(s.name)
print(s.roll_no)

#4
class Shape:
    def area(self):
        return 0


class Rectangle(Shape):
    def area(self):
        return 10 * 5


r = Rectangle()
print(r.area())

#5
class Bird:
    def fly(self):
        print("Bird can fly")


class Penguin(Bird):
    def fly(self):
        print("Penguin cannot fly")


birds = [Bird(), Penguin()]

for b in birds:
    b.fly()