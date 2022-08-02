#!/usr/bin/python3
""" Defining a write to a file function  """


def write_file(filename="", text=""):
    """Write words to a file in utf-8s """

    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
