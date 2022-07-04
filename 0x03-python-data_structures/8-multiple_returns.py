#!/usr/bin/python3

def multiple_returns(sentence):
    lenght = len(sentence)
    if (sentence) == "":
        return(0, None)
    return ("Lenght: {:d} - First character: {}".format(lenght, sentence[0]))
