#!/usr/bin/python3

def new_in_list(my_list, idx: int, element):
    if idx < 0 or idx > len(my_list):
        return my_list
    else:
        another_list = [i for i in my_list]
        another_list[idx] = element
        return another_list
