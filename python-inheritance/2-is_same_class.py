#!/usr/bin/python3
"""
2-is_same_class.py
Module that defines a function is_same_class
"""


def is_same_class(obj, a_class):
    """ Function that returns True if the object is exactly an
    instance of the specified class ; otherwise False."""
    return isinstance(obj, a_class)
