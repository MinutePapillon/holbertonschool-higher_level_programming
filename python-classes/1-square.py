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
    def __init__(self, size):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square's side.

        Private Attributes:
            __size (int):  The size of the square's side.
        """
        self.__size = size
