#!/usr/bin/python3
"""Module defining a Square class with area and print functionality."""

class Square:
    """Class that defines a square."""

    def __init__(self, size=0):
        """Initialize the square with a size (default 0)."""
        self.size = size  # Appelle le setter pour validation

    @property
    def size(self):
        """Getter for retrieving the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for setting the size with type/value checks."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square using '#' character."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):  # Répète size fois
                print("#" * self.__size)  # Affiche une ligne de size caractères
