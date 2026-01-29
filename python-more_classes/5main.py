#!/usr/bin/python3
Rectangle = __import__('5-rectangle').Rectangle

# Création de l'instance
my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

# Suppression de l'instance
del my_rectangle

# Tentative d'accès après suppression
try:
    print(my_rectangle)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
