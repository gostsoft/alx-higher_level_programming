#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):
    if not key == "":
        del a_dictionary[key]
        return a_dictionary
    return a_dictionary
