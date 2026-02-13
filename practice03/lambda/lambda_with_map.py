#1
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

#2
numbers = [1, 2, 3, 4, 5]

# Square every number
squared = list(map(lambda x: x**2, numbers))

print(squared) 
# Output: [1, 4, 9, 16, 25]

#3
words = [" apple ", "banana ", " cherry"]

# Strip whitespace and capitalize
cleaned = list(map(lambda s: s.strip().capitalize(), words))

print(cleaned)
# Output: ['Apple', 'Banana', 'Cherry']

#4
users = [
    {"name": "Alice", "id": 1},
    {"name": "Bob", "id": 2},
    {"name": "Charlie", "id": 3}
]

# Extract just the names
names = list(map(lambda user: user["name"], users))

print(names)
# Output: ['Alice', 'Bob', 'Charlie']

#5
list_a = [1, 2, 3]
list_b = [10, 20, 30]

# Add elements from two lists together
sums = list(map(lambda x, y: x + y, list_a, list_b))

print(sums)
# Output: [11, 22, 33]