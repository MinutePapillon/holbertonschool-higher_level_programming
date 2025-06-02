#!/usr/bin/python3
"""Module that defines the read_file function."""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it."""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
