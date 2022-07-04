#!/usr/bin/python3

def max_integer(my_list=[]):
    max = my_list[0]
    for j in my_list:
        if j > max:
            max = j
    return(max)
