#!/usr/bin/python3
"""
Write a function that creates an Object from a “JSON file
"""


import json


def load_from_json_file(filename):
    """creates an object from json file"""
    with open(filename, encoding="utf-8") as file:
        return json.load(file)
