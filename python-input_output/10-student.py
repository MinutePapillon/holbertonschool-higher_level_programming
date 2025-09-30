#!/usr/bin/python3
"""Student class definition"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve dictionary representation of a Student instance"""
        ordered_keys = ['age', 'last_name', 'first_name']
        result = {}

        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            # Only include attributes from attrs that exist
            for key in ordered_keys:
                if key in attrs and hasattr(self, key):
                    result[key] = getattr(self, key)
        else:
            # Include all attributes in the desired order
            for key in ordered_keys:
                if hasattr(self, key):
                    result[key] = getattr(self, key)

        return result
