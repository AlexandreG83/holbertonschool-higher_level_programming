#!/usr/bin/python3
"""Module that checks exact instance of a class"""


def is_same_class(obj, a_class):
    """Return True if obj is exactly an instance of a_class, False otherwise"""
    return type(obj) is a_class
