#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

# Normal addition
print(add_integer(1, 2))          # 3
print(add_integer(100, -2))       # 98

# Using default value for b
print(add_integer(2))              # 100 (b=98 par défaut)

# Floats converted to integers
print(add_integer(100.3, -2))     # 98 (100 + -2)

# Error: b is not int/float
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)                       # b must be an integer

# Error: a is not int/float
try:
    print(add_integer(None))
except Exception as e:
    print(e)                       # a must be an integer

