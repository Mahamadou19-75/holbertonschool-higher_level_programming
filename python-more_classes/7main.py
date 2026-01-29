#!/usr/bin/python3
Rectangle = __import__('7-rectangle').Rectangle

# Instance 1
my_rectangle1 = Rectangle(8, 4)
print(my_rectangle1)
print("--")

# Changement du print_symbol de l'instance
my_rectangle1.print_symbol = "&"
print(my_rectangle1)
print("--")

# Instance 2
my_rectangle2 = Rectangle(2, 1)
print(my_rectangle2)
print("--")

# Changement du print_symbol de la classe
Rectangle.print_symbol = "C"
print(my_rectangle2)
print("--")

# Instance 3
my_rectangle3 = Rectangle(7, 3)
print(my_rectangle3)
print("--")

# Print symbol de l'instance 3 avec une liste
my_rectangle3.print_symbol = ["C", "is", "fun!"]
print(my_rectangle3)
print("--")

