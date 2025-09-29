#!/usr/bin/python3
"""
1-write_file.py
Module containing function to write a string.
"""


def write_file(filename="", text=""):
    """
    function that writes a string and
    returns the number of characters
    """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
    return len(text)
