#!/usr/bin/python3
"""Basic serialization and deserialization module"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary to JSON and saves it to a file.
    If the file already exists, it should be replaced.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Loads a JSON file and deserializes it into a Python dictionary.
    Returns the dictionary.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
