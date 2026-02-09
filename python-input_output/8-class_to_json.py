#!/usr/bin/python3
"""Module that provides a function to get a dictionary representation of a class instance."""


def class_to_json(obj):
    """Returns the dictionary description of a class instance for JSON serialization."""
    return obj.__dict__
