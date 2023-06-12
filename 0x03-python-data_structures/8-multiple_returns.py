#!/usr/bin/python3

"""
Returns tuple with length of string and first character

Args:
    length: length of sentence
    first: first letter of sentence

Returns:
    tuple with string length and sentence first character
"""


def multiple_returns(sentence):
    length = len(sentence)
    first = sentence[0]
    new_tuple = (length, first)
    if len(sentence) == 0:
        new_tuple = (length, None)
    else:
        new_tuple = (length, first)

    return (new_tuple)
