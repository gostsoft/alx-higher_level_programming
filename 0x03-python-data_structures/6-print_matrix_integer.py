#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    if len(matrix[0]) <= 0:
        print("$")
    for m in matrix:
        for i in m:
            print("{:d}".format(i), end=" " if i != m[-1] else "$")
        print()
