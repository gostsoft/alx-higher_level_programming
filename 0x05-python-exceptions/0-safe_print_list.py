#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    num_of_element = 0
    try:
        for element in range(x):
            print(my_list[element], end="")
            num_of_element += 1
    except IndexError:
        print()
        return num_of_element
    else:
        print()
        return num_of_element
