#!/usr/bin/python3
"""
Module that prints a full name in the format:
My name is <first_name> <last_name>
"""


def say_my_name(first_name, last_name=""):
    """
    Prints My name is <first_name> <last_name>.

    Args:
        first_name (str): first name
        last_name (str, optional): last name. Defaults to "".

    Raises:
        TypeError: if first_name or last_name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}".rstrip())
    
