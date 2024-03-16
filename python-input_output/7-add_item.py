#!/usr/bin/python3
"""
This script adds all arguments to a Python list,
and then saves them to a file named 'add_item.json'.
"""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"


def add_and_save_to_file():
    """
    Load items from a JSON file, extend the list with command-line arguments,
    and save the updated list back to the file.

    If the file doesn't exist, an empty list is created and saved.
    """
    try:
        existing_items = load_from_json_file(filename)
    except FileNotFoundError:
        existing_items = []

    existing_items.extend(sys.argv[1:])
    save_to_json_file(existing_items, filename)


if __name__ == "__main__":
    add_and_save_to_file()
