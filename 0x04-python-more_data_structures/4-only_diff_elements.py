#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    noow = []
    for i, j in zip(set_1, set_2):
        if i !=j:
            noow.append(i)
            noow.append(j)
    return noow
