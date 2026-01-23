#!/usr/bin/python3
"""
Module that prints a text with 2 new lines after '.', '?' and ':'.
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after '.', '?', and ':'.

    Args:
        text (str): text to print

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.strip()
    delimiters = ".?:"
    start = 0
    for i, char in enumerate(text):
        if char in delimiters:
            print(text[start:i + 1].strip())
            print()
            start = i + 1
    remaining = text[start:].strip()
    if remaining:
        print(remaining)
