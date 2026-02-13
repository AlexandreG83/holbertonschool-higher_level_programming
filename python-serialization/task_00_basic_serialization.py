#!/usr/bin/python3
"""Basic serialization module:
Serialize a Python dictionary to a JSON file
Deserialize a JSON file back to a Python dictionary
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary and save it to a JSON file.

    Args:
        data (dict): Python dictionary to serialize.
        filename (str): Output JSON file name.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load and deserialize a JSON file to a Python dictionary.

    Args:
        filename (str): Input JSON file name.

        Returns:
        dict: Python dictionary deserialized from the JSON file.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
