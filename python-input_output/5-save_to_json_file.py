#!/usr/bin/python3
"""Module that defines the save_to_json_file function."""

import json


def save_to_json_file(my_obj, filename):
    with open(filename, "w", encoding="utf-8") as f:
        return json.dump(my_obj, f)
