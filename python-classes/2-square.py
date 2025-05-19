#!/usr/bin/python3
"""
0-square.py
Module containing class Square.
"""


class Square:
    """
    A class to define a square.

    Private Attributes:
        __size (int): The size of the square's side.
    """
    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square's side.

        Private Attributes:
            __size (int):  The size of the square's side.

        Raise:
            TypeError: If size is not an integer
            ValueError: If size is inf to 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
