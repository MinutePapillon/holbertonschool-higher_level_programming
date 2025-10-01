#!/usr/bin/python3
"""Defines a class Student that defines a student by first_name, last_name and age."""


class Student:
    """Student class."""

    def __init__(self, first_name, last_name, age):
        """Initialize student with first_name, last_name and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance.

        - If attrs is a list of strings, only those attributes are retrieved.
        - Otherwise, all attributes are retrieved.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance with those from json.

        Args:
            json (dict): A dictionary of new attribute values.
        """
        for key, value in json.items():
            setattr(self, key, value)
