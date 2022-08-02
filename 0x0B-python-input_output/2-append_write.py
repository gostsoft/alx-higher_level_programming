#!/usr/bin/python3
"""Defining a function that appends a string"""


def append_write(filename="", text=""):
    """Appending a string to a file of text """
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)
