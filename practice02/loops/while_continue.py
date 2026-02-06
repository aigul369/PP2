#1
i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1

#2
i = 1
while i <= 10:
    if i % 2 != 0:
        i += 1
        continue
    print(i)
    i += 1

#3
numbers = [2, -1, 5, -3, 4]
i = 0

while i < len(numbers):
    if numbers[i] < 0:
        i += 1
        continue
    print(numbers[i])
    i += 1

#4
text = "python"
i = 0

while i < len(text):
    if text[i] == "h":
        i += 1
        continue
    print(text[i])
    i += 1

#5
numbers = [0, 1, 2, 0, 3]
i = 0

while i < len(numbers):
    if numbers[i] == 0:
        i += 1
        continue
    print(numbers[i])
    i += 1
