#!/usr/bin/python3


import json

def serialize_and_save_to_file(data, filename):
    """
    Save a Python dictionary to a file as JSON.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    """
    Load JSON data from a file and return it as a Python dictionary.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
