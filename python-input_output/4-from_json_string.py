#!/usr/bin/python3
"""Module that defines the from_json_string function"""


import json


def from_json_string(my_str):
    """
    Returns an object represented by a JSON string.

    Args:
        my_str (JSON string): The JSON string.

    Returns:
        str: The object represented by a JSON string.
    """
    return json.loads(my_str)
