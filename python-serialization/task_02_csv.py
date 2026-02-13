#!/usr/bin/env python3
"""Module for converting CSV data to JSON format."""

import csv
import json


def convert_csv_to_json(filename):
    """
    Converts data from a CSV file to JSON format and writes it to data.json.

    Args:
        filename (str): The CSV file to convert.

    Returns:
        bool: True if successful, False otherwise.
    """
    try:
        data_list = []

        with open(filename, newline='', encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)

            for row in reader:
                data_list.append(row)

        # Serialize and write JSON
        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data_list, json_file)

        return True

    except Exception:
        return False

