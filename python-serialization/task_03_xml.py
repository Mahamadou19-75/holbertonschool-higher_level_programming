#!/usr/bin/env python3
"""Module for serializing and deserializing dictionaries using XML."""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary into an XML file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): XML output file.

    Returns:
        None
    """
    try:
        root = ET.Element("data")

        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)

    except Exception:
        return None


def deserialize_from_xml(filename):
    """
    Deserializes an XML file into a Python dictionary.

    Args:
        filename (str): The XML file to deserialize.

    Returns:
        dict or None: The reconstructed dictionary, or None on failure.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}
        for child in root:
            result[child.tag] = child.text

        return result

    except Exception:
        return None

