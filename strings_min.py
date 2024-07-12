# Demonstrating min() with a string (Example 1)
print(min("aAbByYzZ"))  # Output: 'A'

# Demonstrating min() with a string containing spaces and special characters (Example 2)
t = 'The Knights Who Say "Ni!"'
print('[' + min(t) + ']')  # Output: ' ' (space character)

# Demonstrating min() with a list of numbers (Example 3)
t = [0, 1, 2]
print(min(t))  # Output: 0

# Demonstrating min() with a list of negative numbers (Example 4)
numbers = [-10, -20, -30, -5]
print(min(numbers))  # Output: -30

# Demonstrating min() with a tuple (Example 5)
t = (5, 3, 9, 1)
print(min(t))  # Output: 1

# Demonstrating min() with a list of strings (Example 6)
words = ["apple", "banana", "cherry", "date"]
print(min(words))  # Output: 'apple'

# Demonstrating min() with a list of mixed case strings (Example 7)
mixed_case_words = ["Apple", "banana", "Cherry", "date"]
print(min(mixed_case_words))  # Output: 'Apple'

# Demonstrating min() with a dictionary (Example 8)
d = {'a': 10, 'b': 20, 'c': 5}
print(min(d))  # Output: 'a'
print(min(d.values()))  # Output: 5

# Demonstrating min() with custom key function (Example 9)
words = ["apple", "banana", "cherry", "date"]
print(min(words, key=len))  # Output: 'date'

# Demonstrating min() with multiple arguments (Example 10)
print(min(10, 20, 30, 5, 15))  # Output: 5

# Demonstrating min() with a generator (Example 11)
gen = (x**2 for x in range(10))
print(min(gen))  # Output: 0
