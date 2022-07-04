#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    i = 0
    while i < len(my_list):
        print("{:d} {:s} divisible by 2".format(my_list[i], "is"
                                          if my_list[i] % 2 == 0 else "is not"))
        i += 1
    exit()
