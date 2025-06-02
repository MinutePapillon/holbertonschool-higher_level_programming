#!/usr/bin/python3
"""Module that defines the save_to_json_file function."""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file, using a JS0N representation.

    Args:
        my_obj: The object to srialize and write.
        filename (string): The name of the file where write the text.

    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
