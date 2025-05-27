#!/usr/bin/python3
"""
Module that return if an instance inherited.
"""


def inherits_from(obj, a_class):
    """
    Return True if the objects is an instance of a class
    that inherited from the specified class.
    """
    return type(obj) is not a_class
