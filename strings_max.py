# Demonstrating max() - Example 1:
print(max("aAbByYzZ"))  # Output: 'z'

# Demonstrating max() with a string containing spaces and special characters (Example 2)
t = 'The Knights Who Say "Ni!"'
print('[' + max(t) + ']')  # Output: 'y'

# Demonstrating max() with a list of numbers (Example 3)
t = [0, 1, 2]
print(max(t))  # Output: 2

# Demonstrating max() with a list of negative numbers (Example 4)
numbers = [-10, -20, -30, -5]
print(max(numbers))  # Output: -5

# Demonstrating max() with a tuple (Example 5)
t = (5, 3, 9, 1)
print(max(t))  # Output: 9

# Demonstrating max() with a list of strings (Example 6)
words = ["apple", "banana", "cherry", "date"]
print(max(words))  # Output: 'date'

# Demonstrating max() with a list of mixed case strings (Example 7)
mixed_case_words = ["Apple", "banana", "Cherry", "date"]
print(max(mixed_case_words))  # Output: 'date'

# Demonstrating max() with a dictionary (Example 8)
d = {'a': 10, 'b': 20, 'c': 5}
print(max(d))  # Output: 'c'
print(max(d.values()))  # Output: 20

# Demonstrating max() with custom key function (Example 9)
words = ["apple", "banana", "cherry", "date"]
print(max(words, key=len))  # Output: 'banana'

# Demonstrating max() with multiple arguments (Example 10)
print(max(10, 20, 30, 5, 15))  # Output: 30

# Demonstrating max() with a generator (Example 11)
gen = (x**2 for x in range(10))
print(max(gen))  # Output: 81
