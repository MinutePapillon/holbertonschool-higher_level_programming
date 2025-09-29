#!/usr/bin/python3
"""
5-save_to_json_file.py
Module containing function that returns an object by a JSON.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Function that writes an Object to a text file, using a JSON representation.
    """
    with open(filename, "w", encoding='utf-8') as f:
        json.dump(my_obj, f)
