#!/usr/bin/python3

def magic_calculation(a, b):
    return (a ** b) + 98

import dis
dis.dis(magic_calculation)