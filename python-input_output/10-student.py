#!/usr/bin/python3
"""Module that defines the Student class."""


class Student:
    """Represent a student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list):
            all_str = True
            for attr in attrs:
                if not isinstance(attr, str):
                    all_str = False
                    break

            if all_str:
                result = {}
                for attr in attrs:
                    if hasattr(self, attr):
                        result[attr] = getattr(self, attr)
                return result

        return self.__dict__
