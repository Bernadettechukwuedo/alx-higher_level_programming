#!/usr/bin/python3
def multiple_returns(sentence):
    lent = len(sentence)
    if lent == 0:
        return (0, None)
    return (len(sentence), sentence[0])
