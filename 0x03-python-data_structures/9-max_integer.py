#!/usr/bin/python3
"""
returns max integer

Args:
    maximum is the highest number in the list
    i is the index number for elements in the list

Returns:
    The biggest integer of a list and returns None for empty list
"""


def max_integer(my_list=[]):
    maximum = my_list[0]

    if len(my_list) == 0:
        return (None)
    
    for i in my_list:
        if (i > maximum):
            maximum = i

    return maximum
