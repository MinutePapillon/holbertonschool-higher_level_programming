#!/usr/bin/python3
"""
0-rectangle.py
Module that defines a class Rectangle
"""


class Rectangle:
    """
    A class that defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """"
        Intitalize a new Rectangle instance.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for the private attribute __width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for ___width validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the private attribute __height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for __height validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area"""
        return self.height * self.width

    def perimeter(self):
        """Returns the rectangle perimeter"""
        return (self.height * 2) + (self.width * 2)
