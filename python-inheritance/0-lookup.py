#!/usr/bin/python3
"""
0-lookup.py
Module that defines a function lookup.
"""


def lookup(obj):
    """Function that returns the list of available
    attributes and methods of an object."""
    return dir(obj)
