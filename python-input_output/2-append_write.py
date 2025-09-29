#!/usr/bin/python3
"""
2-append_write.py
Module containing function that appends a string at the end of a text file.
"""


def append_write(filename="", text=""):
    """
    Function that appends a string at the end of a text file.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        f.write(text)
    return len(text)
