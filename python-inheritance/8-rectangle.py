#!/usr/bin/python3
"""
Module that defines the BaseGeometry class.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle that inherits from BaseGeometry.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangle with validated width and height.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
