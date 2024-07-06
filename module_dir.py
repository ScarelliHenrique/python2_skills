#Using the dir() function inside a code may not seem very useful - usually you want to know a particular module's contents before you write and run the code.

import math

# The dir() function returns a list of the names defined in the math module
# This includes functions, constants, and variables available in the module
math_contents = dir(math)

# Displaying the contents of the math module in a more readable way
print("Contents of the math module:")
for item in math_contents:
    print(item)
