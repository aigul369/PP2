#1
i = 1
while i < 6:
  print(i)
  i += 1

#2
i = 5
while i > 0:
    print(i)
    i -= 1

#3
i = 1
total = 0
while i <= 5:
    total += i
    i += 1

print(total)

#4
secret = 3
guess = 0

while guess != secret:
    guess = int(input("Guess: "))

#5
num = 123
rev = 0

while num > 0:
    rev = rev * 10 + num % 10
    num //= 10

print(rev)
