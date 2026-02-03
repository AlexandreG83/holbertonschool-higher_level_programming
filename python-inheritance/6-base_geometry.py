#!/usr/bin/python3
"""Module defining a BaseGeometry class with an area method"""


class BaseGeometry:
    """Represents a base geometry"""

    def area(self):
        """Raise an exception because area is not implemented"""
        raise Exception("area() is not implemented")
