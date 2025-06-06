#!/usr/bin/env python3

import csv
import json


def convert_csv_to_json(filename):
    try:
        with open(filename, mode='r') as file:
            obj = csv.DictReader(file)
            with open("data.json", "w", encoding="utf-8") as file:
                json.dump(list(obj), file)
        return True
    except FileNotFoundError:
        return False
