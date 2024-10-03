#!/usr/bin/env python3
"""
Converting CSV Data to JSON Format
"""
import csv
import json


def convert_csv_to_json(csv_file, json_file='data.json'):
    """
    Takes the CSV filename as its parameter
    and writes the JSON data to data.json.
    """
    try:
        with open(csv_file, 'r',  encoding='utf-8') as csvf:
            csvR = csv.DictReader(csvf)
            data = list(csvR)

        with open(json_file, 'w', encoding='utf-8') as jsonf:
            jsonf.write(json.dumps(data, indent=4))

        return True

    except FileNotFoundError:
        return False
    except Exception:
        return False
