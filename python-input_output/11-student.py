#!/usr/bin/python3
"""Module that defines a Student class with optional attribute filtering."""


class Student:
    """Student class with public attributes and JSON representation."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student with first name, last name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return a dictionary representation of the Student instance.

        If attrs is a list of strings,
        only attributes in this list are included.
        Otherwise, all attributes are returned.
        """
        result = {}
        if isinstance(attrs, list):
            for k, v in self.__dict__.items():
                if k in attrs:
                    result[k] = v
        else:
            result = self.__dict__
        return result

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance using a dictionary.

        json: a dictionary with key = attribute name, value = attribute value
        """
        for key, value in json.items():
            setattr(self, key, value)
