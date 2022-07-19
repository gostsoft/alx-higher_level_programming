#!/usr/bin/python3


class Square:
    """Class - Square"""

    def __init__(self, size=0):
        """Constructor of a Square with the size"""
        if type(size) != int:
            raise (TypeError("size must be an integer"))
        elif size <= 0:
            raise ValueError("size must be an integer")
        else:
            self.__size = size
