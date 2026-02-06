#1
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

#2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#3
numbers = [4, -1, 7, -3, 5]

for num in numbers:
    if num < 0:
        continue
    print(num)


#4
for ch in "python":
    if ch == "h":
        continue
    print(ch)

#5
numbers = [0, 2, 0, 4, 6]

for num in numbers:
    if num == 0:
        continue
    print(num)
