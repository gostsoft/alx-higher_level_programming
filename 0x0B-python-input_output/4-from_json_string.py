#!/usr/bin/python3
"""
Defining a function that returns an object (Python data structure)
represented by a JSON string
"""


import json


def from_json_string(my_str):
    """return json string"""
    return json.loads(my_str)
