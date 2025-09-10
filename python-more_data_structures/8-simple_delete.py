#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    t = False
    for i in a_dictionary:
        if i == key:
            t = True
    if t is True:
        a_dictionary.pop(key)
    return a_dictionary
