#!/usr/bin/python3
"""Defines a Square class with size, position, area, and printing."""


class Square:
    """Represents a square with private size and position attributes."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new Square.

        Args:
            size (int): size of the square (default 0)
            position (tuple): coordinates (x, y) for printing (default (0,0))
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the private size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value (int): new size of the square

        Raises:
            TypeError: if size is not an integer
            ValueError: if size < 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with validation.

        Args:
            value (tuple): tuple of 2 positive integers

        Raises:
            TypeError: if value is not a tuple of 2 positive integers
        """
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with '#' in stdout taking position into account."""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
