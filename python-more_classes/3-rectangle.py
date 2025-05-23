#!/usr/bin/python3

"""
module that create a Rectangle class
"""


class Rectangle():
    """
    a class that represente Rectangle
    """
    def __init__(self, width=0, height=0):
        if (not isinstance(width, int)):
            raise TypeError("width must be an integer")
        if (width < 0):
            raise ValueError("width must be >= 0")
        self.__width = width
        if (not isinstance(height, int)):
            raise TypeError("height must be an integer")
        if (height < 0):
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """
        function that return the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        function set a new width
        """
        if (not isinstance(value, int)):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        function that return the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        function set a new height
        """
        if (not isinstance(value, int)):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        function that return the area of the Rectangle
        """
        return (self.__height * self.__width)

    def perimeter(self):
        """
        function that return the Perimeter of the Rectangle
        """
        if (self.__height == 0 or self.__width == 0):
            return (0)
        return ((self.__height + self.__width) * 2)

    def __str__(self):
        """
        methode that print the square
        """
        rectangle = ""
        if (self.__height == 0 or self.__width == 0):
            return rectangle
        else:
            for row in range(0, self.__height):
                for column in range(0, self.__width):
                    rectangle += "#"
                if (row == self.__height - 1):
                    break
                rectangle += "\n"
        return rectangle
