#!/usr/bin/python3
"""
Module that defines the BaseGeometry class.
"""


class BaseGeometry:
    """
    Base class for geometry-related operations.
    """
    def area(self):
        """
        Calculate the area.

        Raises:
            Exception: Indicates that the method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Valid the integer.

        Raises:
            TypeError: Indicates that name must be an integer.
            ValueError: Indicates that name must be greater than 0.

        Arguments:
            name (str): The name of the value.
            value (int): The value to validate.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
