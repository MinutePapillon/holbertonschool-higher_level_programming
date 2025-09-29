#!/usr/bin/python3
"""
4-from_json_string.py
Module containing function that returns an object by a JSON.
"""

import json


def from_json_string(my_str):
    """
    Function that returns an object.
    """
    return json.loads(my_str)
