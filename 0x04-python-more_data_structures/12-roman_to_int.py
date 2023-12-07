#!/usr/bin/python3

def roman_to_int(roman_string):
    """
    Converts a Roman numeral to an integer.

    Args:
        roman_string: A string representing the Roman numeral.

    Returns:
        An integer equivalent of the Roman numeral.
    """

    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_numeral_map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    integer_value = 0
    for i in range(len(roman_string)):
        current_value = roman_numeral_map[roman_string[i]]
        if i + 1 < len(roman_string) and current_value < roman_numeral_map[roman_string[i + 1]]:
            # Subtraction case
            integer_value -= current_value
        else:
            # Addition case
            integer_value += current_value

    return integer_value
