#!/usr/bin/python3
"""
4-square.py
Module that defines a class Square with size, getter/setter and area method.
"""

class Square:
    """
    A class that defines a square by its size and position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square instance.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for the private attribute __size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for __size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character # and position offset."""
        if self.size == 0:
            print()
            return

        for _ in range(self.position[1]):
            print()

        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)

    @property
    def position(self):
        """Getter for __position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for __position with validation."""
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(i, int) for i in value) or
            not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
