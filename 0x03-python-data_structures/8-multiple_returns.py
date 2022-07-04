#!/usr/bin/python3

def multiple_returns(sentence):
    lenght = len(sentence)
    if (sentence) == "":
        return(0, None)
    return (lenght, sentence[0])
