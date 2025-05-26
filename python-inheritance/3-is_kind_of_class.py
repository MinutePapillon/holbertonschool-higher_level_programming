#!/usr/bin/python3
"""
Module that defines a function to check object inheritance.
"""


def is_kind_of_class(obj, a_class):
    """
    Return True if the object is an instance of, or if
    the object is an instance of a class that inherited from.

    Parameters:
        obj: any object to check
        a_class: the class to compare against

    Returns:
        True if obj is an instance
        """
    return isinstance(obj, a_class)
