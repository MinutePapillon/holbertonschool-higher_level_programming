#!/usr/bin/python3
"""Module that defines the to_json_string function."""


import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj: The Python object to convert to a JSON-formatted string.

    Returns:
        str: the JSON representation.
    """
    return json.dumps(my_obj)
