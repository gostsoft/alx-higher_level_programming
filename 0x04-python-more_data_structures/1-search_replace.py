#!/usr/bin/python3


def search_replace(my_list, search, replace):
    new_list = [i for i in my_list]
    for i in range(len(new_list)):
        if new_list[i] == search:
            new_list[i] = replace
