#!/usr/bin/python3
"""Module that defines the load_from_json function."""

import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The name of file.

    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
