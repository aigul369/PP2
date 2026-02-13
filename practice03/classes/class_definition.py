#1
class MyClass:
  x = 5

#2
p1 = MyClass()
print(p1.x)

#3
p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)

#4
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self) -> str:
        return f"Hi, my name is {self.name} and I am {self.age} years old."
    
#5
from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    in_stock: bool = True

    def apply_discount(self, percent: float) -> None:
        self.price *= (1 - percent / 100)