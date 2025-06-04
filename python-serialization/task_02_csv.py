#!/usr/bin/python3
"""Module to convert CSV data to JSON format."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert a CSV file to JSON format and save to 'data.json'."""
    try:
        with open(csv_filename, mode='r', newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        with open('data.json', mode='w') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except Exception:
        return False
