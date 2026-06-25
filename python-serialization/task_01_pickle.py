#!/usr/bin/python3
"""Module for pickling a custom Python class."""

import pickle


class CustomObject:
    """A custom object with name, age, and is_student attributes."""

    def __init__(self, name, age, is_student):
        """Initialize the object with
        name (str),
        age (int),
        is_student (bool)."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes in a readable format."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance to a file using pickle.

        Args:
            filename (str): The filename to save the object to.
        Returns:
            None if an exception occurs.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize a CustomObject instance from a pickle file.

        Args:
            filename (str): The filename to load the object from.
        Returns:
            CustomObject instance or None if an exception occurs.
        """
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
            return obj
        except Exception:
            return None
