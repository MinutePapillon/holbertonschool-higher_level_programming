#!/usr/bin/python3
"""
Module that defines the Student class.
"""


class Student:
    """
    Represent a student with first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Get a dict of the student's data.

        If attrs is a list of strings, return only those.
        Else, return all data.
        """
        if isinstance(attrs, list):
            all_strings = True
            for attr in attrs:
                if not isinstance(attr, str):
                    all_strings = False
                    break

            if all_strings:
                result = {}
                for attr in attrs:
                    if hasattr(self, attr):
                        result[attr] = getattr(self, attr)
                return result

        return self.__dict__

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student using a dictionary.

        Args:
            json (dict): Dictionary with new attribute values.
        """
        for key, value in json.items():
            setattr(self, key, value)
