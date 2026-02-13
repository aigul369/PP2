#1
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)

#2
words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)

#3
words = ["banana", "apple", "kiwi", "cherry"]

# Sort by the length of each word
by_length = sorted(words, key=lambda s: len(s))

print(by_length)
# Output: ['kiwi', 'apple', 'banana', 'cherry']

#4
numbers = [-10, 5, -2, 8, 1]

# Sort by absolute value
absolute_sort = sorted(numbers, key=lambda x: abs(x))

print(absolute_sort)
# Output: [1, -2, 5, 8, -10]

#5
products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 25},
    {"name": "Monitor", "price": 300}
]

# Sort by price in descending order
cheapest_first = sorted(products, key=lambda p: p["price"], reverse=True)

print(cheapest_first)
# Output: [{'name': 'Laptop', 'price': 1200}, {'name': 'Monitor', 'price': 300}, ...]