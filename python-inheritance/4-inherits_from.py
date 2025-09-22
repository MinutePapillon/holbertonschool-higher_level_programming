#!/usr/bin/python3
"""
4-inherits_from.py
Module that defines a function inherits_from.
"""


def inherits_from(obj, a_class):
    """
    Function that returns True if the object is an instance.

    Args:
        obj (): the instance to verify.
        a_class (): the class for verify.

    Returns:
        True: if the object is an instance.
        False: otherwise.
    """
    if type(obj) is not a_class and isinstance(obj, a_class):
        return True
    else:
        return False
