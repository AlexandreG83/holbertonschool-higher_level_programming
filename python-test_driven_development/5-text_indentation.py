#!/usr/bin/python3
"""
Module that prints a text with 2 new lines after '.', '?' and ':'.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':' characters.
    No spaces at the beginning or end of each printed line.

    Args:
        text: A string to process and print

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    line = ""
    for char in text:
        line += char
        if char in '.?:':
            print(line.strip())
            print()
            line = ""
    if line.strip():
        print(line.strip(), end="")
