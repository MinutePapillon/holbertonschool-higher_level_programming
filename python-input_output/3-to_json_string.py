#!/usr/bin/python3
"""
3-to_json_string.py
Module containing function that returns the JSON representation of an object.
"""

import json


def to_json_string(my_obj):
    """
    Function that returns the JSON representation.
    """
    return json.dumps(my_obj)
