#!/usr/bin/python3
"""Module that defines a Square class inheriting from Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(Rectangle):
    """Square class inheriting from Rectangle"""

    def __init__(self, size):
        """Initialize a square with size"""
        BaseGeometry.integer_validator(self, "size", size)
        self.__size = size
        super().__init__(size, size)
