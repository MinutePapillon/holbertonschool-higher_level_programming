#!/usr/bin/python3
"""
0-read_file.py
Module containing function to read a file.
"""


def read_file(filename=""):
    """Reads a UTF-8 text file and prints its content to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
