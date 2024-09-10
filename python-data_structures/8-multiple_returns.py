#!/usr/bin/python3
def multiple_returns(sentence):
    first = sentence[0]
    lenght = len(sentence)
    if sentence == "":
        return (0, None)
    else:
        return (lenght, first)
