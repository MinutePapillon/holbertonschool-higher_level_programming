#!/usr/bin/python3
"""
3-is_kind_of_class.py
Module that defines a function is_kind_of_class.
"""


def is_kind_of_class(obj, a_class):
    """
    Function that returns True if the object is an instance.

    Args:
        obj (): the instance to verify.
        a_class (): the class for verify.

    Returns:
        True: if the object is an instance.
        False: otherwise.
    """
    return isinstance(obj, a_class)
