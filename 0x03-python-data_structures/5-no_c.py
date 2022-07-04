#!/usr/bin/python3


def no_c(my_string):
    name = [i for i in my_string if i != "c" if i != "C"]
    return("".join(name))
