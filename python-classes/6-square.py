#!/usr/bin/python3
"""Square class with size and position attributes."""


class Square:
    """Class that defines a square with optional size and position."""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size          # Utilise le setter
        self.position = position  # Utilise le setter

    @property
    def size(self):
        """Getter for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position with validation."""
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not isinstance(value[0], int) or
            not isinstance(value[1], int) or
            value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with # character, considering the position."""
        if self.__size == 0:
            print()
            return

        # Ajoute les lignes vides si position[1] > 0
        for _ in range(self.__position[1]):
            print()

        # Affiche chaque ligne du carré
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
