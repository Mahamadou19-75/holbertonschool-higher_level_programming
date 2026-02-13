#!/usr/bin/env python3
"""Module for serializing and deserializing a custom class using pickle."""

import pickle


class CustomObject:
    """A custom class representing a person with serialization features."""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Displays the object's attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the object and saves it to the given filename.

        Args:
            filename (str): The file where the object will be saved.

        Returns:
            None
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Loads and returns a serialized CustomObject instance from file.

        Args:
            filename (str): The file to load the object from.

        Returns:
            CustomObject or None: The loaded object, or None on failure.
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
                if isinstance(obj, cls):
                    return obj
                return None
        except Exception:
            return None

