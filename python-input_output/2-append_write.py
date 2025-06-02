#!/usr/bin/python3
"""Module that defines the append_write function"""


def append_write(filename="", text=""):
    """
    Add a text in a text file and return the number of character written.

    Args:
        filename (str): the name of file to write.
        text (str): The text to write into the file.

    Returns:
        int: The number of character written.
    """
    with open(filename, "a", encoding="UTF-8") as f:
        return f.write(text)
