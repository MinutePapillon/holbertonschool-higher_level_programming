#!/usr/bin/python3
"""
7-base_geometry.py
Module that defines a class BaseGeometry.
"""


class BaseGeometry:
    """
    Empty class.
    """
    def area(self):
        """
        Function that raises.

        Args:
            self (): the instance.

        Raises:
            raises an Exception with the message area() is not implemented.

        Returns:
            Nothing.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Function that validates value.

        Args:
            name (str): the argument.
            value (int): the number.

        Raises:
            if value is not an integer: raise a TypeError exception.
            if value is less or equal to 0: raise a ValueError exception.

        Returns:
            Nothing.
            """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
