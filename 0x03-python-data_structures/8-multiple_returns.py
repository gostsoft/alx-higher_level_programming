#!/usr/bin/python3

def multiple_returns(sentence):
    lenght = len(sentence)
    if len(sentence) == 0:
        return ("Lenght: {:d} - First character: {}".format(lenght, None))
    else:
         return ("Lenght: {:d} - First character: {}".format(lenght, sentence[0]))
