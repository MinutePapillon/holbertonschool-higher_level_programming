#!/usr/bin/env python3
import json


def serialize_and_save_to_file(data, filename):
    fichier.write(json.dumps(data))


def load_and_deserialize(filename):
    with open(filename, 'r', encoding="UTF-8") as fichier:
        result = fichier.read()
    return json.loads(result)
