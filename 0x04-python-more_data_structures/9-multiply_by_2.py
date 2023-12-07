#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for key, value in sorted(a_dictionary.items()):
        new_value = value * 2
        dict = {key: new_value}
        new_dictionary.update(dict)
    return new_dictionary
