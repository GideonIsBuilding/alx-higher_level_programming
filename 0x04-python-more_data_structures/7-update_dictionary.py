#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    temp_dict = a_dictionary.copy()
    for items in temp_dict.items():
        if key not in temp_dict.items():
            new_dict = {key: value}
            a_dictionary.update(new_dict)
    return a_dictionary
