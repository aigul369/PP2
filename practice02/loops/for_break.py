#1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

#3

for i in range(1, 10):
    if i == 5:
        break
    print(i)

#4
for ch in "python":
    if ch == "h":
        break
    print(ch)

#5
items = ["pen", "book", "eraser"]

for item in items:
    if item == "book":
        break
    print(item)
