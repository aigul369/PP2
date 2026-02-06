#1
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#2
secret = 7

while True:
    guess = int(input("Guess: "))
    if guess == secret:
        break

#3
while True:
    num = int(input("Enter number: "))
    if num < 0:
        break

#4
numbers = [2, 4, 6, 8, 10]
i = 0

while i < len(numbers):
    if numbers[i] == 6:
        break
    i += 1

#5
while True:
    password = input("Password: ")
    if password == "abc123":
        break
