#1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#2
for x in "banana":
  print(x)

#3
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#4
total = 0
for i in range(1, 6):
    total += i

print(total)

#5
for x in range(6):
  print(x)
else:
  print("Finally finished!")