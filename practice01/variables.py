#1
x = 5
y = "John"
print(x)
print(y)

#2
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#3
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#4
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#5
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)