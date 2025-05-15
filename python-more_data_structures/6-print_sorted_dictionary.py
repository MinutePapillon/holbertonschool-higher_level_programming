#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dictionary = {}
    keys = a_dictionary.keys()
    sorted_keys = sorted(keys)
    for key in sorted_keys:
        sorted_dictionary[key] = a_dictionary[key]
    for i, j in sorted_dictionary.items():
        print(f"{i}: {j}")
