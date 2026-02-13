#1
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

#2
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

#3
x = Student("Mike", "Olsen")
x.printname()

#4
class Animal:
    def speak(self):
        print("The animal makes a sound")


class Dog(Animal):
    def bark(self):
        print("The dog barks")


dog = Dog()
dog.speak()   # inherited method
dog.bark()    # child method

#5
class Animal:
    def speak(self):
        print("The animal speaks")


class Cat(Animal):
    def speak(self):
        print("The cat meows")


animal = Animal()
cat = Cat()

animal.speak()
cat.speak()   # overridden