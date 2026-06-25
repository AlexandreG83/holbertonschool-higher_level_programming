#!/usr/bin/python3
"""Convert CSV data to JSON format."""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file to JSON and save it to data.json.

    Args:
        csv_filename (str): Input CSV file name.

    Returns:
        bool: True if conversion is successful, False otherwise.
    """
    try:
        with open(csv_filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]

        with open('data.json', mode='w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)

        return True

    except Exception:
        return False
