#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    integer = 0
    prev = 0
    for i in roman_string:
        current = roman[i]
        if prev < current:
            integer += current - 2 * prev
        else:
            integer += current
        prev = current
    return integer
