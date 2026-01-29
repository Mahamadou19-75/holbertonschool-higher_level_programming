#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

# Création d'un carré via la méthode de classe
mysquare = Rectangle.square(5)

# Affichage de l'aire et du périmètre
print("Area: {} - Perimeter: {}".format(mysquare.area(), mysquare.perimeter()))

# Affichage du carré avec le print_symbol
print(mysquare)
