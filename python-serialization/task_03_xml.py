#!/usr/bin/python3
"""Module for serializing and deserializing Python dictionaries using XML."""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to XML and save to a file.

    Args:
        dictionary (dict): Dictionary to serialize.
        filename (str): Output XML filename.
    """
    data_root = ET.Element('data')
    for key, value in dictionary.items():
        item = ET.SubElement(data_root, key)
        item.text = str(value)
    xml_tree = ET.ElementTree(data_root)
    xml_tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserialize an XML file into a Python dictionary.

    Args:
        filename (str): XML filename to read.
    Returns:
        dict: Deserialized dictionary.
    """
    try:
        xml_tree = ET.parse(filename)
        data_root = xml_tree.getroot()
        dict_data = {}
        for item in data_root:
            dict_data[item.tag] = item.text
        return dict_data
    except Exception:
        return None
