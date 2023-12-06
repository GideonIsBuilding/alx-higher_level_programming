#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    div = []
    for num in my_list:
        if num % 2 == 0:
            div.append(1)
        else:
            div.append(0)
    return div
