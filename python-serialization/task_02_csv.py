#!/usr/bin/python3
import csv
import json


def convert_csv_to_json(filename):
    """
    Convert a CSV file into a JSON file named 'data.json'
    Returns True if successful, False otherwise
    """
    try:
        with open(filename, mode="r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        with open("data.json", mode="w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except Exception:
        return False
