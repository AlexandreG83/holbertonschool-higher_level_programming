#!/usr/bin/python3
"""Module defining a BaseGeometry class with area and integer validation"""


class BaseGeometry:
    """Represents a base geometry"""

    def area(self):
        """Raise an exception because area is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer

        Args:
            name (str): name of the parameter (used in error messages)
            value (any): value to validate

        Raises:
            TypeError: if value is not an integer
            ValueError: if value <= 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
