#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    length = len(my_list)
    if idx < 0:
        return None
    elif idx > length - 1:
        return None
    else:
        my_list[idx] = element
    return (my_list)

my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
