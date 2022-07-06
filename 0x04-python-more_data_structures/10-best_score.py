#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary:
        highest_score = max(list(a_dictionary.values()))
        for key, value in a_dictionary.items():
            if highest_score == value:
                return (key)
    return None
