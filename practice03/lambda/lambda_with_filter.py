#1
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

#2
numbers = [1, 5, 8, 10, 13, 16, 20]

# Keep only numbers greater than 10
large_numbers = list(filter(lambda x: x > 10, numbers))

print(large_numbers)
# Output: [13, 16, 20]

#3
products = [
    {"name": "Laptop", "price": 1200, "in_stock": True},
    {"name": "Mouse", "price": 25, "in_stock": False},
    {"name": "Monitor", "price": 300, "in_stock": True}
]

# Only keep items that are in stock
available = list(filter(lambda p: p["in_stock"], products))

print(available)
# Output: [{'name': 'Laptop', ...}, {'name': 'Monitor', ...}]

#4
data = ["Admin", "", "Editor", None, "Guest", 0]

# Filter out anything that evaluates to False
clean_data = list(filter(lambda x: bool(x), data))

print(clean_data)
# Output: ['Admin', 'Editor', 'Guest']

#5
tags = ["python", "js", "php", "java", "c", "ruby"]

# Only keep tags with more than 3 characters
long_tags = list(filter(lambda s: len(s) > 3, tags))

print(long_tags)
# Output: ['python', 'java', 'ruby']