#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len((my_list)) - 1:
        return my_list
    new_list = [i for i in my_list if i != my_list[idx]]
    my_list.clear()
    for j in new_list:
        my_list.append(j)
    return new_list
