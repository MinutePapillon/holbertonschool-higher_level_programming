#!/usr/bin/python3
"""Module that defines the write_file function"""


def write_file(filename="", text=""):
    """
    Write a string to a test file and returns the number of character written.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to write into the file.

    Returns:
        int: The number of character written.
    """
    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)
