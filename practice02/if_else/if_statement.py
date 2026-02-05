#1
a = 33
b = 200
if b > a:
  print("b is greater than a")

#2
number = 15
if number > 0:
  print("The number is positive")

#3
age = 20
if age >= 18:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")

#4
is_logged_in = True
if is_logged_in:
  print("Welcome back!")

#5
numbers = [1, 3, 5, 8, 9]

if (n := len(numbers)) > 5:
    print(f"List is long: {n} elements")
else:
    print(f"List is short: {n} elements")
